import cv2 
import numpy as np 
import glob 
import matplotlib.pyplot as plt 

def xycuts(img_file):
	name = img_file.split('/')[-1].split('.')[0]
	count = [] # maintain a black count 
	img = cv2.imread(img_file, 0)
	fig, ax = plt.subplots()
	height, width = img.shape
	print(width)
	for ix in range(height):
		if(img[ix].sum()/255 > 750): # we count horizontal if greater than 750. 
			ax.axhline(y=ix, linewidth=2, color='black')
		else:
			for iy in range(width):
				if(img[ix][iy] == 0):
					count.append(iy)
	if len(count) != 0: # if we get blacks, then draw vertical lines at minimum and maximum.
		ax.axvline(x=min(count), linewidth=2, color='black')
		ax.axvline(x=max(count), linewidth=2, color='black')
	ax.imshow(img, cmap='gray')
	plt.savefig("x_y_cuts_{}.png".format(name))

if __name__ == '__main__':
	xycuts("lab3 Images/XY-cutss.png")