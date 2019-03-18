'''
	We implement a histogram equalization technique in this task on a greyscale image. 
'''
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import collections


pdf = []
cdf = list(np.zeros(256))
transformation_ftn = []

def plot_histogram(img):
	plt.hist(img.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
	plt.title("Histogram of {}".format("Equalized Image"))
	plt.show()

def hist_equalization(img):
	height, width = img.shape 
	hist_equalized_img = np.zeros(shape=img.shape)
	img_flatten = np.ravel(img)
	freq_dict = collections.Counter(img_flatten)
	for ix in range(256):
		if ix not in freq_dict.keys():
			freq_dict[ix] = 0
	freq_dict = collections.OrderedDict(sorted(freq_dict.items()))
	for key, value in freq_dict.iteritems():
		pdf.append(float(value)/((height*width)))
	for ix in range(len(pdf)):
		try:
			cdf[ix] = pdf[ix] + cdf[ix-1]
		except:
			cdf[ix] = pdf[ix]
	for ix in range(len(cdf)):
		transformation_ftn.append(round(cdf[ix]*255))
	for y in range(height):
		for x in range(width):
			pixel = img[x,y]
			img[x,y] = transformation_ftn[pixel]
	plot_histogram(img)
	plt.imshow(img, cmap='gray')
	plt.show()
	
def main(img_file):
	img = cv2.imread(img_file, 0)
	hist_equalization(img)

main("hist2.tif")
