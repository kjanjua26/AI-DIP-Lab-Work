'''
	Image enhancement of a washed out image using few techniques. 
'''
import cv2
import matplotlib.pyplot as plt 
import numpy as np 

def plot_histogram(img):
	plt.hist(img.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
	plt.show()
	
def gamma_correction(img_file, gamma=0.2):
	'''
		This is technique number 01. 
		We apply gamma correction to check the results of the enhanced washed out image.
	'''	
	img = cv2.imread(img_file, 0)
	height, width = img.shape 
	gamma_corrected_img = np.zeros(shape=img.shape)
	print("Height: ", height, " Width: ", width)
	for y in range(width-1):
		for x in range(height-1):
			gamma_corrected_img[x,y] = (1*img[x,y]**(1/gamma))*255
	plt.imshow(gamma_corrected_img, cmap='gray')
	plt.show()

def histogram_equalization(img_file):
	'''
		This is the technique number 02. 
		We apply histogram equalization technique in this to image.
		'''
	img = cv2.imread(img_file)
	img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
	img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
	img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
	plt.imshow(img_output)
	plt.show()
	plot_histogram(img_output)

histogram_equalization("sample_img.jpg")
