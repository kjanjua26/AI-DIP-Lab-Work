"""
	Bit Plane Slicing 
"""
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 

def threshold_image(img, threshold):
	return np.where(img>threshold, 1, 0)

def bit_plane_slicing(img_file, plane_level):
	img = cv2.imread(img_file, 0)
	plane_level = 1
	transformed_img = np.zeros(shape=img.shape)
	height, width = img.shape
	for slice_factor in range(8):
		for y in range(height):
			for x in range(width):
				try:
					if img[x,y] & plane_level == 0:
						transformed_img[x,y] = 0
					else:
						transformed_img[x,y] = 1
				except:
					pass
		plane_level *= 2
		cv2.imwrite("{}_sliced.png".format(slice_factor), transformed_img)
		plt.imshow(transformed_img, cmap='gray')
		plt.show()
bit_plane_slicing("dollar.tif", plane_level=1)
