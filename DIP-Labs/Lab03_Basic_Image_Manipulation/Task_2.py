import cv2 
import numpy as np 
import glob 
import matplotlib.pyplot as plt 

vals_dict = {}
def histogram(img_file):
	name = img_file.split('/')[-1].split('.')[0]
	img = cv2.imread(img_file)
	img_flatten = np.ravel(img, np.int32)
	containers = np.zeros(256, np.int32)
	for pix in img_flatten:
		containers[pix] += 1
	containers = containers/3 # because we use RGB image to compute 
	for index, vals in enumerate(containers):
		vals_dict[index] = vals
	plt.bar(vals_dict.keys(), vals_dict.values(), color='black')
	plt.xlabel("Grey Levels")
	plt.ylabel("Intensity")
	plt.title("For Document: {}".format(name))
	plt.savefig("histogram_{}.png".format(name))


def caller():
	for file in glob.glob("lab3 Images/Document/*.jpg"):
		histogram(file)

if __name__ == '__main__':
	caller()
