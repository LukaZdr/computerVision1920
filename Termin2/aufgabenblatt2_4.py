#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
img = imread("./catG.png")
plt.imshow(img, cmap="Greys_r")

#Aufgabe 4

plt.imshow(np.invert(img), cmap="Greys_r") # invertieren des bildes
plt.imshow(np.flip(img,1),cmap="Greys_r") # horizontales spiegeln des bildes

plt.imshow(img[20:275, 250:500],cmap="Greys_r") # katzenkopf abtrennen