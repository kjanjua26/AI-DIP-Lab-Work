import cv2
import matplotlib.pyplot as plt
import numpy as np


def erosion(img, kernel):
    eroded_img = cv2.erode(img, kernel, iterations=1)
    plt.imshow(eroded_img, cmap="gray")
    plt.show()

def dilation(img, kernel):
    dilated_img = cv2.dilate(img, kernel, iterations=1)
    plt.imshow(dilated_img, cmap="gray")
    plt.show()

def invert(img):
    invert_img = (255-img)
    return invert_img

img = cv2.imread("signature.png", 0)
img = invert(img)
kernel = np.ones((5, 5), np.uint8)
erosion(img, kernel)
dilation(img, kernel)
