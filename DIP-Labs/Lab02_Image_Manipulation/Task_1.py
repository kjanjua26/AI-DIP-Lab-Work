import PIL 
from PIL import Image 
import os, sys
print "For: ", sys.argv[1]
im = Image.open(sys.argv[1])
print "Format: ", im.format
print "Size: ", im.size 
print "Mode: ", im.mode
#im.show()

print "Converting to JPEG"
file = sys.argv[1]
name, path = file.split('.')
outfile = name + '.jpg'
try:
	Image.open(file).save(outfile)
	print "Converted Image"
except IOError:
	print "cannot convert", file
