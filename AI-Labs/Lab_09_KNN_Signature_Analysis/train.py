import numpy as np
from glob import glob
from main import *
import cv2
from utils import bounding_box
#from scipy.spatial.distance import euclidean

# Reference Files
centroids = {}
transitions = {}
ratios = {}
black_sizes = {}
angles = {}
normalization = {}
normalized_sums = {}

# Questioned Data
q_black_sizes = {}
q_angles = {}
q_centroids = {}
q_ratios = {}
q_transitions = {}
q_normalization = {}
q_normalized_sums = {}

def fillReferenceData():
    for folder in glob("/Users/Janjua/Desktop/BSCS/Artificial Intelligence/Labs/Lab09/Features/*"):
        for files in glob(folder+"/*"):
            reference_file_name = files.split('/')[-1]
            file_name = reference_file_name.split('.')[0].split('_')[0]
            with open(files, "r+") as open_reference_file:
                feature_vector = open_reference_file.readlines()
                feature_vector = [x.replace('\n', '') for x in feature_vector]
                if "normalized_sums.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    normalized_sums[file_name] = feature_vector
                if "angles.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    angles[file_name] = feature_vector
                if "ratios.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    ratios[file_name] = feature_vector
                if "centroids.txt" in reference_file_name:
                    auxilary_list = []
                    for x in feature_vector:
                        cx, cy = x.split(',')
                        cx = cx.replace('(', '').replace(' ', '')
                        cy = cy.replace(')', '').replace(' ', '')
                        point = (float(cx), float(cy))
                        auxilary_list.append(point)
                    centroids[file_name] = auxilary_list
                if "normalized.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    normalization[file_name] = feature_vector
                if "black_size.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    black_sizes[file_name] = feature_vector
                if "transitions.txt" in reference_file_name:
                    feature_vector = [float(x) for x in feature_vector]
                    transitions[file_name] = feature_vector

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

def euclidean(ref, ques):
    try:
        squares = [(p-q) ** 2 for p, q in zip(ref, ques)]
        return sum(squares) ** .5
    except:
        auxilary_list = []
        for x in range(len(ref)):
            ref_x1, ref_y1 = ref[x]
            ques_x2, ques_y2 = ques[x]
            centroid_distance = math.sqrt(((ref_x1-ques_x2)**2)+((ref_y1-ques_y2)**2))
            auxilary_list.append(centroid_distance)
    return np.mean(auxilary_list)

def calculateDistance():
    distance_file = open('distance.csv', 'w')
    distance_file.write('Ref,Question,Ratio,Transitions,Black_Size,Normalization,Normalization_Sums,Angles,Centroid')
    distance_file.write('\n')
    for ref in ratios.keys():
        for question in q_ratios.keys():
            ratio_distance = str(euclidean(ratios[ref], q_ratios[question]))
            transitions_distance = str(euclidean(transitions[ref], q_transitions[question]))
            black_sizes_distance = str(euclidean(black_sizes[ref], q_black_sizes[question]))
            normalization_distance = str(euclidean(normalization[ref], q_normalization[question]))
            normalization_sums_distance = str(euclidean(normalized_sums[ref], q_normalized_sums[question]))
            angles_distance = str(euclidean(angles[ref], q_angles[question]))
            centroid_distance = str(euclidean(centroids[ref], q_centroids[question]))
            print("The distance of centroids between {} and {} is: {}".format(ref, question, centroid_distance))
            print("The distance of ratios between {} and {} is: {}".format(ref, question, ratio_distance))
            print("The distance of transitions between {} and {} is: {}".format(ref, question, transitions_distance))
            print("The distance of angle between {} and {} is: {}".format(ref, question, angles_distance))
            print("The distance of black sizes between {} and {} is: {}".format(ref, question, black_sizes_distance))
            print("The distance of normalization between {} and {} is: {}".format(ref, question, normalization_distance))
            print("The distance of normalization sums between {} and {} is: {}".format(ref, question, normalization_sums_distance))
            print()
            toWrite = ref+','+question+','+ratio_distance+','+transitions_distance+','+black_sizes_distance+','+normalization_distance+','+normalization_sums_distance+','+angles_distance+','+centroid_distance+'\n'
            distance_file.write(toWrite)
    distance_file.close()

if __name__ == "__main__":
    fillReferenceData()
    fillQuestionData()
    print("Done reading data")
    calculateDistance()
