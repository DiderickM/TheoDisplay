#!/usr/bin/python

# A more complex RGBMatrix example works with the Python Imaging Library,
# demonstrating a few graphics primitives and image loading.
# Note that PIL graphics do not have an immediate effect on the display --
# image is drawn into a separate buffer, which is then copied to the matrix
# using the SetImage() function (see examples below).
# Requires rgbmatrix.so present in the same directory.

# PIL Image module (create or load images) is explained here:
# http://effbot.org/imagingbook/image.htm
# PIL ImageDraw module (draw shapes to images) explained here:
# http://effbot.org/imagingbook/imagedraw.htm

import Image
import ImageDraw
import time
import numpy as np
import pprint
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 2)

# Bitmap example w/graphics prims
image = Image.new("RGB", (64, 32)) # Can be larger than matrix if wanted!!
image.resize = ((10,10))
draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
# Draw some shapes into image (no immediate effect on matrix)...

left_top = (0, 64)
right_top = (32, 64)
right_top_bottom = (32, 48)
right_top_middle = (20, 48)
right_bottom_right = (24, 16)
bottom = (16, 0)
left_bottom_left = (8, 16)
left_top_middle = (12, 48)
left_top_bottom = (0, 48)

x = np.array((left_top, right_top, right_top_bottom, right_top_middle, right_bottom_right, bottom, left_bottom_left, left_top_middle, left_top_bottom))
y = np.matrix(((0,1), (-1, 0)))
z = np.array(((64,0)))
rotate = ((x * y)+z)


pp = pprint.PrettyPrinter(depth=6)
rotateA = np.squeeze(np.asarray(rotate))
rotateB = tuple(map(tuple, rotateA))

original = (left_top, right_top, right_top_bottom, right_top_middle, right_bottom_right, bottom, left_bottom_left, left_top_middle, left_top_bottom)
pp.pprint(rotateB)

draw.polygon((rotateB), fill=(255,20,147), outline=3)

# Then scroll image across matrix...
for n in range(-32, 0): # Start off top-left, move off bottom-right
	matrix.Clear()
	# IMPORTANT: *MUST* pass image ID, *NOT* image object!
	matrix.SetImage(image.im.id, n, n)
	time.sleep(0.1)
time.sleep(1)
image.im.resize((20,20))


for i in range(1, 10):
	matrix.Clear()
	time.sleep(0.5)
	matrix.SetImage(image.im.id, -1, -1)
	time.sleep(0.5)
time.sleep(1)
matrix.Clear()
