import numpy as np
from glob import glob
from main import *
import cv2
from utils import bounding_box

# Reference Files
centroids = {}
transitions = {}
ratios = {}
black_sizes = {}
angles = {}
normalization = {}
normalized_sums = {}

# Questioned Data
q_rectangles = {}
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
            with open(files, "r+") as open_reference_file:
                print("For Reference File: \n", reference_file_name)
                feature_vector = open_reference_file.readlines()
                if "normalized_sums.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    normalized_sums[file_name] = feature_vector
                if "angles.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    angles[file_name] = feature_vector
                if "ratios.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    ratios[file_name] = feature_vector
                if "centroids.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    centroids[file_name] = feature_vector
                if "normalized.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    normalization[file_name] = feature_vector
                if "black_size.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    black_sizes[file_name] = feature_vector
                if "transitions.txt" in reference_file_name:
                    file_name = reference_file_name.split('.')[0].split('_')[0]
                    transitions[file_name] = feature_vector

def fillQuestionData():
    pass
