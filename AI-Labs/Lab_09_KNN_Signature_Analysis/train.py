import numpy as np
from glob import glob
from utils import *

centroids = {}
transitions = {}
ratios = {}
black_sizes = {}
angles = {}
normalization = {}
normalized_sums = {}

for folder in glob("/Users/Janjua/Desktop/BSCS/Artificial Intelligence/Labs/Lab09/Features/*"):
    for files in glob(folder+"/*"):
        reference_file_name = files.split('/')[-1]
        with open(files, "r+") as open_reference_file:
            print("For Reference File: \n", reference_file_name)
            feature_vector = open_reference_file.readlines()
            print(len(feature_vector))
            print("")
