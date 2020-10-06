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
image = Image.open('test2_copy.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
matrix.Fill(0x000000)
for n in range(-32, 0, 1):
	matrix.Clear()
	matrix.SetImage(im.im.id, n, n)
	time.sleep(0.1)
	
time.sleep(1)

# Bitmap example w/graphics prims
image = Image.open('handen2.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
matrix.Fill(0x000000)
for n in range(-20, 60, 1):
	matrix.SetImage(im.im.id, n, 0)
	time.sleep(0.08)
	matrix.Clear()

# Bitmap example w/graphics prims
image = Image.open('Theo_copy.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
matrix.Fill(0x000000)
for n in range(-200, 40, 1):
	matrix.SetImage(im.im.id, 0, n)
	time.sleep(0.02)
	matrix.Clear()


image = Image.open('test2_copy.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
for n in range(0, 186, 6):
	matrix.Clear()
	if n < 90:
		sizeMultiplier = -1.0
		base = 1.0
	else:
		sizeMultiplier = 1.0
		base = 0.0
	size = (base+((sizeMultiplier*n)/180.0))
	imRotate = im.resize([int(size*im.size[0]),int(size*im.size[1])])	
	imRotate = imRotate.rotate(n, Image.NEAREST, 1)
	
	matrix.SetImage(imRotate.im.id, 0, 0)
	time.sleep(0.05)

im = im.rotate(180, Image.NEAREST, 1)

for n in range(0, 186, 6):
	matrix.Clear()
	if n < 90:
		sizeMultiplier = -1.0
		base = 1.0
	else:
		sizeMultiplier = 1.0
		base = 0.0
	size = base+((sizeMultiplier*n)/180.0)
	imRotate = im.resize([int(size*im.size[0]),int(size*im.size[1])])
	imRotate = imRotate.rotate(n, Image.NEAREST, 1)
	
	matrix.SetImage(imRotate.im.id, 0, 0)
	time.sleep(0.05)	
	
time.sleep(1)
matrix.Clear()
