import numpy as np 
import matplotlib.pyplot as plt 
import cv2 
from itertools import product


def threshold_binarization(img, threshold=150):
	height, width = img.shape
	for i,j in product(range(height), range(width)):
		if img[i][j] > threshold:
			img[i][j] = 0
		else:
			img[i][j] = 1
	return img

def connected_component_labelling(img):
	height, width = img.shape
	blackScore = 1
	img = np.array(img); mask = np.array(img)
	min_values = []; max_values = []
	v_set = 0
	background = 0
	for i, j in product(range(height), range(width)):
	        if img[i][j] > background:
	            x_updated = mask[i][j-1]
	            y_updated = mask[i-1][j]
	            if x_updated > background and y_updated > background:
	                    if x_updated != y_updated:
	                        mask[i][j] = min(x_updated, y_updated)
	                        if max(x_updated, y_updated) not in min_values:
	                            min_values.append(max(x_updated, y_updated))
	                            max_values.append(min(x_updated, y_updated))
	                        else:
	                            index_ = min_values.index(max(x_updated, y_updated))
	                            if max_values[index_] > min(x_updated, y_updated):
	                                intensity_ = max_values[index_]
	                                max_values[index_] = min(x_updated, y_updated)
	                                while intensity_ in min_values and v_set < 100:
	                                    v_set += 1
	                                    index_ = min_values.index(intensity_)
	                                    intensity_ = max_values[index_]
	                                    max_values[index_] = min(x_updated, y_updated)
	                                min_values.append(intensity_)
	                                max_values.append(min(x_updated, y_updated))
	                    else:
	                        mask[i][j] = max(x_updated, y_updated)
	            elif x_updated > background and y_updated < background:
	                mask[i][j] = x_updated
	            elif x_updated < background and y_updated > background:
	                mask[i][j] = y_updated
	            else:
	                mask[i][j] = blackScore
	                blackScore += 1
	v_set = 1
	for idx, val in enumerate(min_values):
	    if max_values[idx] in min_values and v_set < 100:
	        v_set += 1
	        index_ = min_values.index(max_values[idx])
	        max_values[idx] = max_values[index_]

	for i,j in product(range(1, len(mask)), range(1, len(mask[0]))):
	        if mask[i][j] in min_values:
	            index_ = min_values.index(mask[i][j])
	            mask[i][j] = max_values[index_]
	return mask

def run():
	img = cv2.imread("Lab4-image.png", 0)
	img = threshold_binarization(img)
	img = connected_component_labelling(img)
	plt.imshow(img, cmap='gray')
	plt.savefig("result.png")
	plt.title('Connected Component Labelling Result')
	plt.show()

if __name__ == '__main__':
	run()
