'''
    In this we implement local histogram equalization in sliding window fashion. 
'''
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import collections
def plot_histogram(img, name):
    plt.hist(img.ravel(), bins=256, range=(0.0, 255.0))
    plt.title("Histogram of {} image".format(name))
    plt.show()

def sliding_window_eq(img_file):
    img = cv2.imread(img_file, 0)
    window = 8
    height, width = img.shape 
    hook_image = img.copy()
    for y in range(height-window):
        for x in range(width-window):
            window_eq = cv2.equalizeHist(img[y:y+window, x:x+window].copy())
            hook_image[y:y+window, x:x+
            window] = window_eq
    plt.imshow(hook_image, cmap='gray')
    plt.show()
    plot_histogram(hook_image, "sliding (128) Eq.")

sliding_window_eq("sample.png")
