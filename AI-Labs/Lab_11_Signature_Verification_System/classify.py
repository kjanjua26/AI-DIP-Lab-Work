import numpy as np
from glob import glob
from main import *
import cv2
from utils import bounding_box
import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.manifold import TSNE
import matplotlib
import matplotlib.pyplot as plt
import random

# Questioned Data
q_black_sizes = {}
q_angles = {}
q_centroids = {}
q_ratios = {}
q_transitions = {}
q_normalization = {}
q_normalized_sums = {}
key = {}
hashed_key = ['F', 'D', 'G']
x = []
y = []

def fillQuestionData():
    for folder in glob("/Users/Janjua/Desktop/BSCS/Artificial Intelligence/Labs/Lab09/QFeatures/*"):
        for files in glob(folder+"/*"):
            question_file_name = files.split('/')[-1]
            file_name = question_file_name.split('.')[0].split('_')[0]
            with open(files, "r+") as open_question_file:
                feature_vector = open_question_file.readlines()
                feature_vector = [x.replace('\n', '') for x in feature_vector]
                if "normalized_sums.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_normalized_sums[file_name] = feature_vector
                if "angles.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_angles[file_name] = feature_vector
                if "ratios.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_ratios[file_name] = feature_vector
                if "centroids.txt" in question_file_name:
                    auxilary_list = []
                    for x in feature_vector:
                        cx, cy = x.split(',')
                        cx = cx.replace('(', '').replace(' ', '')
                        cy = cy.replace(')', '').replace(' ', '')
                        point = (float(cx), float(cy))
                        auxilary_list.append(point)
                    q_centroids[file_name] = auxilary_list
                if "normalized.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_normalization[file_name] = feature_vector
                if "black_size.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_black_sizes[file_name] = feature_vector
                if "transitions.txt" in question_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    q_transitions[file_name] = feature_vector
def train():
    fillQuestionData()
    key_dataframe = pd.read_csv('key.csv')
    ques_ = list(key_dataframe['QuestionSig'].dropna())
    ques_ = [int(x) for x in ques_]
    res = list(key_dataframe['Decision'].dropna())
    for points in range(len(ques_)):
        key[str(ques_[points])] = res[points]
    for ix, data in enumerate(q_normalization.keys()):
        dec_holder = str(re.findall(r'\d+', data)).replace('[', '').replace(']', '').replace("'", '').lstrip('0')
        x.append(q_ratios[data]+q_black_sizes[data]+q_transitions[data]+q_normalization[data]+q_normalized_sums[data]+q_angles[data])
        if 'F' in key[dec_holder]:
            y.append(0)
        if 'D' in key[dec_holder]:
            y.append(1)
        if 'G' in key[dec_holder]:
            y.append(2)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    train_list = list(zip(X_train, y_train))
    random.shuffle(train_list)
    shuff_x_train, shuff_y_train = zip(*train_list)
    test_list = list(zip(X_test, y_test))
    random.shuffle(test_list)
    shuff_x_test, shuff_y_test = zip(*test_list)
    print(shuff_y_train)
    assert len(shuff_x_train) == len(shuff_y_train)
    assert len(shuff_x_test) == len(shuff_y_test)

    tree = DecisionTreeClassifier(random_state=0)
    tree.fit(shuff_x_train, shuff_y_train)
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(shuff_x_train, shuff_y_train)
    print('Accuracy using Decision Tree: ', tree.score(shuff_x_train, shuff_y_train))
    print('Accuracy using kNN (k = 3): ', neigh.score(shuff_x_train, shuff_y_train))

    X_embedded = TSNE(n_components=2).fit_transform(shuff_x_test)
    x_list = [x for [x, y] in X_embedded]
    y_list = [y for [x, y] in X_embedded]
    plt.scatter(x_list, y_list, c=shuff_y_test)
    plt.title('TSNE Plot of Features')
    plt.savefig('tsne.png')
    plt.show()

if __name__ == "__main__":
    train()
