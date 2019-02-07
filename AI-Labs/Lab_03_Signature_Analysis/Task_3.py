import cv2 
from PIL import Image, ImageDraw
import numpy as np 
"""
We implement centroid locating algorithm on the cropped image
"""
img = cv2.imread("cropped_image.png")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray_image,127,255,0)
M = cv2.moments(thresh)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.imwrite("centroids_image.png", img)
