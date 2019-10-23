#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
img = imread("./catG.png")
plt.imshow(img, cmap="Greys_r")

# Aufgabe 2
# 1

schwarze_pix = 0
weiße_pix = 0 
for zeile in range(img.shape[0]):
    for spalte in range(img.shape[1]):
        pixel = img[zeile,spalte]
        if pixel == 0: schwarze_pix +=1
        if pixel == 255: weiße_pix +=1
        
print("weiße pixel sind:",  weiße_pix, "schwarze pixel sind:" , schwarze_pix)

# 2
graustufen_count = {}
    
for zeile in range(img.shape[0]):
    for spalte in range(img.shape[1]):
        pixel = img[zeile,spalte]
        if pixel in graustufen_count:
            graustufen_count[pixel] += 1
        else:
            graustufen_count[pixel] = 1
        
print(graustufen_count)

print(sum(graustufen_count.values())) # test das alle sum von values = zahl aller pixel
