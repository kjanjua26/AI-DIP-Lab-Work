import numpy as np
import cv2
import sys
import math

from utils import *
from glob import glob

rectangles = []
black_sizes = []
angles = []
centroids = []
ratios = []
transitions = []
normalization = []
normalized_sums = []

def binarization(img):
	retval, binarized_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
	return binarized_img

def split(image, left, right, top, bottom, depth=0):
    cx, cy = findCentroid(image, left, right, top, bottom)
    if depth < 3:
        split(image, left, cx, top, cy, depth + 1)
        split(image, cx, right, top, cy, depth + 1)
        split(image, left, cx, cy, bottom, depth + 1)
        split(image, cx, right, cy, bottom, depth + 1)
    else:
        rectangles.append([(left, top), (right, bottom)])
        size = (bottom-top)*(right-left)
        blacks = findBlacks(image, left, right, top, bottom)
        try:	
            black_sizes.append(size/blacks)
        except:
            black_sizes.append(0)
        if blacks == 0:
            normalization.append(0)
        else:
            normalization.append(((right-left)*(bottom-top)/blacks))
        if cx == left:
            angle = math.pi / 2
        else:
            angle = math.atan((float)((bottom-cy) / (float)(cx-left)))
        angles.append(angle)
        centroids.append((cx, cy))
        ratios.append((right-left)/(bottom-top))
        transitions.append(findTransitions(image, left, right, top, bottom))
        normalized_sums.append(blackPixelAngleSummation(image, left, top, right, bottom))


if __name__ == "__main__":
    for img_file in glob("/Users/Janjua/Desktop/BSCS/Artificial Intelligence/Labs/Lab09/Dataset_4NSigComp2010/TestSet/Reference/*.png"):
        img_name = img_file.split('/')[-1].split('.')[0]
        print("For {}\n".format(img_name))
        img = cv2.imread(img_file, 0)

        img = binarization(img)
        top, bottom, right, left = bounding_box(img)
        print('Spliting...')
        rectangles = []
        black_sizes = []
        angles = []
        centroids = []
        ratios = []
        transitions = []
        normalization = []
        normalized_sums = []
        
        split(img, left, right, top, bottom)
        print(len(rectangles))

        blacks_out = open("Features/Black_Size/"+str(img_name)+'_black_size.txt', 'w')
        angles_out = open("Features/Angles/"+str(img_name)+'_angles.txt', 'w')
        transitions_out = open("Features/Transitions/"+str(img_name)+'_transitions.txt', 'w')
        centroids_out = open("Features/Centroids/"+str(img_name)+'_centroids.txt', 'w')
        ratios_out = open("Features/Ratios/"+str(img_name)+'_ratios.txt', 'w')
        normalized_blacks = open("Features/Normalized_Blacks/"+str(img_name)+'_normalized.txt', 'w')
        normalized_angle_sums = open("Features/Angle_Sums/"+str(img_name)+'_normalized_sums.txt', 'w')
        print('Writing to files...')

        for i in range(len(rectangles)):
            img = cv2.rectangle( img, (rectangles[i][0][0], rectangles[i][0][1]), (rectangles[i][1][0], rectangles[i][1][1]), (0,0,0), 1)
            centroids_out.write(str(centroids[i])+'\n')
            transitions_out.write(str(transitions[i])+'\n')
            ratios_out.write(str(ratios[i])+'\n')
            blacks_out.write(str(black_sizes[i])+'\n')
            angles_out.write(str(angles[i])+'\n')
            normalized_blacks.write(str(normalization[i])+'\n')
            normalized_angle_sums.write(str(normalized_sums[i])+'\n')
