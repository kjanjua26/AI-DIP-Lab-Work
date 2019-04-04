'''
    In this task we perform the salt and pepper noise removal using median filtering.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def medianFilter(img_file, filter_size):
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    size = filter_size//2
    hook_img = img.copy()
    img = np.pad(img, size, 'constant', constant_values=0)
    for y in range(size, height-size):
        for x in range(size, width-size):
            filtered_window = img[y-size:y+size+1, x-size:x+size+1]
            filtered_window = np.sort(filtered_window, axis=None)
            hook_img[y-size,x-size] = filtered_window[filter_size**2 // 2]
    
    plt.imshow(hook_img, cmap="gray")
    plt.show()

medianFilter("saltandpaper.tif", 5)