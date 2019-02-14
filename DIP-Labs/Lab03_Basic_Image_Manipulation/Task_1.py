import cv2 
import numpy as np 
import glob 

threshold_array = [100, 128, 150, 200, 220]
def threshold_binarization(img_file, threshold):
	name = img_file.split('/')[-1].split('.')[0]
	img = cv2.imread(img_file, 0)
	bin_img = np.where(img>threshold, 255, 0)
	cv2.imwrite("lab3 Images/Document/{}_bin_{}.png".format(name, threshold), bin_img)

def caller():
	for file in glob.glob("lab3 Images/Document/*.*"):
		for threshold in threshold_array:
			threshold_binarization(file, threshold)

if __name__ == '__main__':
	caller()