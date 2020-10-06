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

# Levels vliegt voorbij
image = Image.open('images/Levels.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
matrix.Fill(0x000000)
for n in range(-295, 40, 1):
	matrix.SetImage(im.im.id, 0, n)
	time.sleep(0.02)
matrix.Clear()


# Basis
image = Image.open('images/Levels_klein.png') # Can be larger than matrix if wanted!!
image.load()
im = image.rotate(90)
imbase = im
matrix.Fill(0x000000)

# Invliegen van onder

for n in range(-64, -29, 2):
	matrix.Clear()
	matrix.SetImage(im.im.id, -n, 0)
	time.sleep(0.08)

time.sleep(0.5)

# 3 en 5 logo's

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

# Flash all

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

# Sequence 1 flash

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 8, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 8, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
time.sleep(0.04)
matrix.Clear()


matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.3)
matrix.Clear()

# Sequence 3 flash

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.03)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.03)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.03)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.03)
matrix.Clear()


matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(1.2)
matrix.Clear()

# Sequence 2 flash

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 19, 0)
time.sleep(0.05)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
time.sleep(0.05)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 19, 0)
time.sleep(0.05)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
time.sleep(0.05)
matrix.Clear()


matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.8)
matrix.Clear()

# Sequence 3/5 flash

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 8, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 52, 0)
matrix.SetImage(im.im.id, 30, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 8, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 52, 0)
matrix.SetImage(im.im.id, 30, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 8, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(0.3)
matrix.SetImage(im.im.id, 52, 0)
matrix.SetImage(im.im.id, 30, 0)
time.sleep(0.04)
matrix.Clear()

enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 8, 0)
enh = ImageEnhance.Brightness(imbase)
im = enh.enhance(1)
matrix.SetImage(im.im.id, 52, 0)
matrix.SetImage(im.im.id, 30, 0)
time.sleep(0.04)
matrix.Clear()


matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.5)
matrix.Clear()

# Flash all

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

# 5-4-3-2-1

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
matrix.SetImage(im.im.id, 52, 0)
time.sleep(0.1)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
matrix.SetImage(im.im.id, 41, 0)
time.sleep(0.1)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
matrix.SetImage(im.im.id, 30, 0)
time.sleep(0.1)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
matrix.SetImage(im.im.id, 19, 0)
time.sleep(0.1)

matrix.Clear()
matrix.SetImage(im.im.id, 8, 0)
time.sleep(0.1)

matrix.Clear()



# 3 rijen
# 
# matrix.Clear()
# matrix.SetImage(im.im.id, 19, 0)
# matrix.SetImage(im.im.id, 30, 0)
# matrix.SetImage(im.im.id, 41, 0)
# time.sleep(0.5)
# 
# Vlieg boven uit
# 
# for n in range(-28, 7, 2):
# 	matrix.Clear()
# 	matrix.SetImage(im.im.id, -n, 0)
# 	time.sleep(0.08)



