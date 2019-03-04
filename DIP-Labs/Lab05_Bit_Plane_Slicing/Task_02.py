import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def threshold_image(img, threshold):
	return np.where(img>threshold, 1, 0)

def gradient_edge_detection(img_file):
	img = cv2.imread(img_file, 0)
	bin_img = threshold_image(img, 128)
	transformed_array = np.zeros(shape=bin_img.shape)
	height, width = bin_img.shape
	for y in range(height):
		for x in range(width):
			try:
				diff = abs(bin_img[x+1,y]-bin_img[x,y])
			except:
				pass
			if diff == 1:
				transformed_array[x,y] = diff
	plt.imshow(transformed_array, cmap='gray')
	plt.show()

gradient_edge_detection("lena_color.png")
