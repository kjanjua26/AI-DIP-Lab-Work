import numpy as np
import cv2
import sys
import math
import matplotlib.pyplot as plt
#from utils import *
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
    retval, binarized_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    return binarized_img

def bounding_box(img):
    height, width = img.shape
    left, right = width, 0
    top, bottom = height, 0

    for x in range(width):
        for y in range(height):
            color = img[y, x]
            if color == 0:
                if x > right:
                    right = x
                if x < left:
                    left = x 
                if y > bottom:
                    bottom = y
                if y < top:
                    top = y

    print("The bounding box is:")
    print("Top: ", top, " Bottom: ", bottom, " Left: ", left, " Right: ", right)
    return top, bottom, right, left

def findCentroid(img, left, right, top, bottom):
    cx, cy, n = 0, 0, 0
    for x in range(left, right):
        for y in range(top, bottom):
            if img[y,x] == 0:
                cx = cx + x 
                cy = cy + y
                n += 1
    if n == 0:
        return cx, cy		
    cx = cx // n
    cy = cy // n
    return cx, cy

def findTransitions(img, left, right, top, bottom):
    height, width = img.shape
    prevPixel = img[0,0]
    countBW = 0
    for x in range(left, right):
        for y in range(top, bottom):
            curPixel = img[y,x]
            if (curPixel == 255) and (prevPixel == 0):
                countBW += 1
            prevPixel = curPixel
    return countBW

if __name__ == "__main__":
    img_file = "/Users/Janjua/Desktop/BSCS/Digital Image Processing/Labs/Lab12/Signature.png"
    img_name = img_file.split('/')[-1].split('.')[0]
    print("For {}\n".format(img_name))
    img = cv2.imread(img_file, 0)
    
    img = binarization(img)
    top, bottom, right, left = bounding_box(img)
    cx, cy = findCentroid(img, left, right, top, bottom)
    print('The centroid is at: ', cx, cy)
    top_left_trans = findTransitions(img, left, cx, top, cy)
    top_right_trans = findTransitions(img, cx, right, top, cy)
    bottom_left_trans = findTransitions(img, left, cx, cy, bottom)
    bottom_right_trans = findTransitions(img, cx, right, cy, bottom)
    print('Computing transitions.')
    print('The top left is: ', top_left_trans)
    print('The bottom left is: ', bottom_left_trans)
    print('The top right is: ', top_right_trans)
    print('The bottom right is: ', bottom_right_trans)
    centeroid_image = cv2.circle(img, (cy, cx), 10, 200, -1)
    cut_img = cv2.rectangle(img, (left, top), (cx, cy), (0,255,0), 3)
    cut_img = cv2.rectangle(cut_img, (cx, top), (right, cy), (0,255,0), 3)
    cut_img = cv2.rectangle(cut_img, (left, cy), (cx, bottom), (0,255,0), 3)
    cut_img = cv2.rectangle(cut_img, (cx, cy), (right, bottom), (0,255,0), 3)

    plt.imshow(cut_img, cmap='gray')
    plt.show()
    cv2.imwrite('out.png', cut_img)