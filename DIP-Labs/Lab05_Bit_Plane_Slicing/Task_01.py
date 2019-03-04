import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def threshold_image(img, threshold):
	return np.where(img>threshold, 255, 0)

def negative_transformation_method(img_file, toNotBin, file_type):
	if 'RGB' in file_type:
		img = cv2.imread(img_file)
		transformed_array = np.zeros(shape=img.shape)
		height, width, channels = img.shape
		for y in range(height):
			for x in range(width):
				red = abs(255-img[x,y][0]-1)
				green = abs(255-img[x,y][1]-1)
				blue = abs(255-img[x,y][2]-1)
				transformed_array[x,y] = [red,green,blue]
		cv2.imwrite("rgb_inversed.png", transformed_array)
	else:
		if toNotBin:
			img = cv2.imread(img_file,0)
			transformed_array = np.zeros(shape=img.shape)
			height, width = img.shape
			for y in range(height):
				for x in range(height):
					inv = abs(255-img[x,y]-1)
					transformed_array[x,y] = inv
			cv2.imwrite("grey_scaled_inversed.png", transformed_array)
		else:
			img = cv2.imread(img_file,0)
			bin_img = threshold_image(img, 128)
			transformed_array = np.zeros(shape=bin_img.shape)
			height, width = bin_img.shape
			for y in range(height):
				for x in range(height):
					inv = abs(255-img[x,y]-1)
					transformed_array[x,y] = inv
			cv2.imwrite("bin_inversed.png", transformed_array)

negative_transformation_method("lena_color.png", toNotBin=False, file_type="RGB")
