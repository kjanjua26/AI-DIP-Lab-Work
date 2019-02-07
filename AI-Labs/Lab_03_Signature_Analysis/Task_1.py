import cv2 
import numpy as np 

"""
  Reading image, and converting to black and white. 
  We use OTSU binarization for the task.
"""
img_file = "test.jpg"
img = cv2.imread(img_file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grey_sig.png", img_gray)
retval2,threshold = cv2.threshold(img_gray,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("otsu_bin_sig.png", threshold)
