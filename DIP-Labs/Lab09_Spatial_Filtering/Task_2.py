'''
    In this task we implement the Gaussian filtering.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def gaussianFilter(img_file, filtersize):
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    hook_img = img.copy()
    given_filter = [[1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0], 
                    [1.0, 2.0, 2.0, 4.0, 2.0, 2.0, 1.0], 
                    [2.0, 2.0, 4.0, 8.0, 4.0, 2.0, 2.0],
                    [2.0, 4.0, 8.0, 16.0, 8.0, 4.0, 2.0],
                    [2.0, 2.0, 4.0, 8.0, 4.0, 2.0, 2.0],
                    [1.0, 2.0, 2.0, 4.0, 2.0, 2.0, 1.0],
                    [1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0]]  
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            sum_given = np.matrix(given_filter).sum()
            #given_filter = (np.divide(given_filter, sum_given))
            #given_filter = np.multiply(given_filter, 255)
            convolved_filter = np.matmul(filtered_window, given_filter)
            hook_img[y:y+filtersize, x:x+filtersize] = convolved_filter
    plt.imshow(hook_img, cmap="gray")
    plt.show()

gaussianFilter("smoothing.tif", 7)