from PIL import Image, ImageDraw
import numpy as np 
"""
We implement bounding box algorithm for the OTSU binarized image.
"""
img_file = "otsu_bin_sig.png"
img = Image.open(img_file)
img = img.convert("RGBA")
width, height = img.size
image_data = img.load()
pixel = [width, height]
end = [0,0]

for y in xrange(height):
	for x in xrange(width):
	  if image_data[x, y][0] < 200 and image_data[x, y][1] < 200 and image_data[x, y][2] < 200:
		if x < pixel[0]:
		  pixel[0] = x
		if y < pixel[1]:
		  pixel[1] = y
		if x > end[0]:
		  end[0] = x
		if y > end[1]:
		  end[1] = y

bounding_box = (pixel[0], pixel[1], end[0], end[1])
bounded_box_img = img.crop(bounding_box)
bounded_box_img.save("cropped_image.png")
draw_rect = ImageDraw.Draw(img)
draw_rect.rectangle(((pixel[0], pixel[1]),(end[0], end[1])), outline="black")
img.save("detected_box.png")
