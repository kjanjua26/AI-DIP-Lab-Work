'''
    In this we implement local histogram equalization in tiling fashion. 
'''
import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import collections

def plot_histogram(img, name):
    plt.hist(img.ravel(), bins=256, range=(0.0, 255.0))
    plt.title("Histogram of {} image".format(name))
    plt.show()

def tiliing_fashion_equalization(img_file):
    img = cv2.imread(img_file, 0)
    height, width = img.shape 
    mid_point = [height/2, width/2] # the midpoint of the image to crop it in 4 sections
    tiles = []
    tiled_images = []
    tiled_eq_images = []
    for i in range(height/mid_point[0]):
        for j in range(width/mid_point[1]):
            box = (j*mid_point[1], i*mid_point[0], (j+1)*mid_point[1], (i+1)*mid_point[0]) 
            tiles.append(box)
    print(tiles)
    for i in range(len(tiles)):
        tiled_images.append(img[tiles[i][0]:tiles[i][2], tiles[i][1]:tiles[i][3]])
        plt.imshow(img[tiles[i][0]:tiles[i][2], tiles[i][1]:tiles[i][3]], cmap='gray')
        plt.show()
        plot_histogram(img[tiles[i][0]:tiles[i][2], tiles[i][1]:tiles[i][3]], i)

    for i in tiled_images:
        tiled_eq_images.append(cv2.equalizeHist(i.copy()))
    print(tiled_eq_images)
    top = np.vstack((tiled_eq_images[0], tiled_eq_images[1]))
    bottom = np.vstack((tiled_eq_images[2], tiled_eq_images[3]))
    equalized_tiling_images = np.hstack((top, bottom))
    plt.imshow(equalized_tiling_images, cmap="gray")
    plt.show()
    plot_histogram(equalized_tiling_images, "tiled Eq")    

if __name__ == "__main__":
    tiliing_fashion_equalization("sample.png")
