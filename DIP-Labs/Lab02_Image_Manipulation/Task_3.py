import PIL 
from PIL import Image 
import os, sys
from PIL import ImageFilter
import numpy as np 
from matplotlib.image import imread 
import matplotlib.pyplot as plt 

print "Manipulation For: ", sys.argv[1]

print "a. Conversion of RGB to Greyscale!"
img = Image.open(sys.argv[1])
img = img.convert('LA')
img.save('Greyscale_lena.png')

print "b. Smoothing filter"
img = Image.open(sys.argv[1])
smoothImage = img.filter(ImageFilter.SMOOTH)
smoothImage.save('smoothLena.png')

print "c. Sharpening filter"
img = Image.open(sys.argv[1])
sharpImage = img.filter(ImageFilter.SHARPEN)
sharpImage.save('sharpLena.png')

print "d. RGB to Greyscale (no library)"
img_np = imread(sys.argv[1])
grey_img_np = np.dot(img_np, [0.299, 0.587, 0.114])
plt.imsave('custom_grey_scale_lena.png', grey_img_np, cmap='gray')