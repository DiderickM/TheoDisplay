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
import ImageEnhance
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 2)

# Bitmap example w/graphics prims
image = Image.open('images/Levels_klein.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
imbase = im
matrix.Fill(0x000000)
for n in range(-64, -29, 2):
	matrix.Clear()
	matrix.SetImage(im.im.id, -n, 0)
	time.sleep(0.08)

time.sleep(0.5)

matrix.Clear()
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.5)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.5)

matrix.Clear()

for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
	
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
	
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
		
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

matrix.Clear()
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.15)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.15)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.15)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.15)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.15)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.15)




for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
	
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
	
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()
		
for f in range(-10, -2, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(-f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

for f in range(2, 10, 1):
	enh = ImageEnhance.Brightness(imbase)
	im = enh.enhance(float(f)/10)
	matrix.SetImage(im.im.id, 8, 0)
	matrix.SetImage(im.im.id, 19, 0)
	matrix.SetImage(im.im.id, 30, 0)
	matrix.SetImage(im.im.id, 41, 0)
	matrix.SetImage(im.im.id, 52, 0)
	time.sleep(0.03)
	matrix.Clear()

matrix.Clear()
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.5)



for n in range(-28, 7, 2):
	matrix.Clear()
	matrix.SetImage(im.im.id, -n, 0)
	time.sleep(0.08)

matrix.Clear()

