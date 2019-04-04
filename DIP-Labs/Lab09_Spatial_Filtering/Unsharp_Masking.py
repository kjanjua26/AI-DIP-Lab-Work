'''
    In this task we implement the unsharp masking.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def averagingFilter(img, filtersize):
    height, width = img.shape
    hook_img = img.copy()
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            filtered_window = np.ravel(filtered_window)
            avg = (sum(filtered_window))/(filtersize*filtersize)
            hook_img[y:y+filtersize, x:x+filtersize] = avg
    return hook_img

def weightedFilter(img, filtersize):
    height, width = img.shape
    hook_img = img.copy()
    given_filter = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            convolved_filter = np.matmul(filtered_window, given_filter)
            hook_img[y:y+filtersize, x:x+filtersize] = convolved_filter
    return hook_img

def unsharpMasking(img_file, filtersize):
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    smooth_img = weightedFilter(img, filtersize)
    diff_img = img.copy()
    res_img = img.copy()
    for y in range(height):
        for x in range(width):
            diff = img[y, x] - smooth_img[y, x]
            diff_img[y, x] = diff
    for y in range(height):
        for x in range(width):
            add_res = diff_img[y, x] + smooth_img[y, x]
            res_img[y,x] = add_res
    plt.imshow(res_img, cmap="gray")
    plt.show()

unsharpMasking("unsharpmasking.tif", 3)