'''
    In this task we apply MOG2 background subtraction.
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

def threshold_binarize(img):
    return np.where(img>45, 255, 0)

def imshow_components(labels):
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    labeled_img[label_hue==0] = 0
    plt.imshow(labeled_img, cmap='nipy_spectral')
    plt.show()

def main(img_file):
    img = cv2.imread(img_file, 0)
    bin_img = threshold_binarize(img)
    bin_img = bin_img.astype('uint8')
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    fgbg = cv2.createBackgroundSubtractorMOG2()
    fgmask = fgbg.apply(bin_img)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    plt.imshow(255-fgmask, cmap='gray')
    plt.show()
    kernel = np.ones((3, 3), np.uint8)
    _, labels = cv2.connectedComponents(255-fgmask)
    imshow_components(labels)

main("sample.png")
