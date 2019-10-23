#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
img = imread("./catG.png")
plt.imshow(img, cmap="Greys_r")

# Aufgabe 1

x = len(img) # höhe des bildes => 525
y = len(img[0]) # breite des bildes => 700
pixel_count =  x*y # anzahl der pixel

print(pixel_count)

max_pix = max(map(lambda x: max(x), img)) # maximum des bildes => 255
min_pix = min(map(lambda x: min(x), img)) # minimum des bildes => 
mean_pix =  sum(map(lambda x: sum(x), img)) / pixel_count 

print(max_pix)
print(min_pix)
print(mean_pix)
plt.imshow(img, cmap="Greys_r")
