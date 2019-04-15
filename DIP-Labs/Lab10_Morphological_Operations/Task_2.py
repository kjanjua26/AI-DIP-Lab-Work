import cv2
import matplotlib.pyplot as plt
import numpy as np

def binarization(img):
    bin_img = np.where(img>45, 255, 0)
    return bin_img

def invert(img):
    invert_img = (255-img)
    return invert_img

def compoundOperation(img):
    bin_img = binarization(img)
    inv_bin_img = invert(bin_img)
    inv_bin_img = inv_bin_img.astype('uint8')
    kernel = np.ones((5, 5), np.uint8)
    dilated_img = cv2.dilate(inv_bin_img, kernel, iterations=2)
    plt.imshow(dilated_img, cmap="gray")
    plt.show()

img = cv2.imread("urduSig.png", 0)
compoundOperation(img)
