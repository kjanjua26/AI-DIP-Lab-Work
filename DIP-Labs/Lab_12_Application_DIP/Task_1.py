import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_processing(img_file):
    img = cv2.imread(img_file, 0)
    ret, img = cv2.threshold(img, 127, 255, 0)
    skel = np.zeros(img.shape, np.uint8)
    size = np.size(img)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    done = False
    while not done:
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()
        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True
    skel = 255 - skel
    blur = cv2.GaussianBlur(skel, (7,7), 0)
    plt.imshow(blur, cmap='gray')
    plt.show()
    cv2.imwrite('thinned_image.png', skel)

apply_processing("ThumbImpression.png")
