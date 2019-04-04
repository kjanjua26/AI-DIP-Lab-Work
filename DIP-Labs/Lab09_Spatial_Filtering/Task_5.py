'''
    In this task we perform the horizontal and vertical edge detection.
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def edgeDetection(img_file, filterType, filtersize):
    if filterType == "Horizontal":
        given_filter = [[1, 1, 1], [0, 0, 0], [-1, -1, -1]]
    else:
        given_filter = [[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]
    img = cv2.imread(img_file, 0)
    height, width = img.shape
    hook_img = img.copy()
    for y in range(height-filtersize):
        for x in range(width-filtersize):
            filtered_window = img[y:y+filtersize, x:x+filtersize]
            convolved_filter = np.matmul(filtered_window, given_filter)
            hook_img[y:y+filtersize, x:x+filtersize] = convolved_filter
    plt.imshow(hook_img, cmap="nipy_spectral")
    plt.title(filterType)
    plt.show()
    return hook_img

horizontal_filtered = edgeDetection("two_cats.jpg", "Horizontal", 3)
vertical_filtered = edgeDetection("two_cats.jpg", "Vertical", 3)
plt.imshow(vertical_filtered+horizontal_filtered, cmap="gray")
plt.title("Edge Detected")
plt.show()