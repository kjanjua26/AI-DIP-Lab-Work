'''
    In this task we implement the averaging filter with varying sizes.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def averagingFilter(img_file, filtersize):
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    hook_img = img.copy()
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            filtered_window = np.ravel(filtered_window)
            avg = (sum(filtered_window))/(filtersize*filtersize)
            hook_img[y:y+filtersize, x:x+filtersize] = avg
    plt.imshow(hook_img, cmap="gray")
    plt.show()

def weightedFilter(img_file, filtersize):
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    hook_img = img.copy()
    given_filter = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            convolved_filter = np.matmul(filtered_window, given_filter)
            hook_img[y:y+filtersize, x:x+filtersize] = convolved_filter
    plt.imshow(hook_img, cmap="gray")
    plt.show()

weightedFilter("smoothing.tif", 3)
