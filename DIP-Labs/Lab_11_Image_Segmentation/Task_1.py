'''
  In this task we apply the following pipeline to segment: Binarize => Image Morphology => CCL
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

def otsu_binarize(img):
    _, otsu_binarized_img = cv2.threshold(img, 240, 255, cv2.THRESH_OTSU)
    return otsu_binarized_img

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
    plt.imshow(bin_img, cmap='gray')
    plt.show()
    kernel = np.ones((3, 3), np.uint8)
    erosion_img = cv2.erode(bin_img, kernel, iterations=1)
    dilation = cv2.dilate(erosion_img, kernel, iterations=2)
    plt.imshow(dilation, cmap='gray')
    plt.show()
    _, labels = cv2.connectedComponents(dilation)
    imshow_components(labels)

main("sample.png")
