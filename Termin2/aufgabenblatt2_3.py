#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
img = imread("./catG.png")
plt.imshow(img, cmap="Greys_r")

print("x und y",img.shape) # breite und höhe
print(np.prod(img.shape)) # anzahl der pixel
print(np.amin(img)) # minimum
print(np.amax(img)) # maximum
print(np.mean(img)) # mittelwert
