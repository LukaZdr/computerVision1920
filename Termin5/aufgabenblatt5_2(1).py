# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:07:28 2019

@author: MightyA
"""

#Aufgabe 5_2



import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import filters


#5.2.1
img_cat = imread('./catG.png')


cat_sobel_h = filters.sobel_h(img_cat)
cat_sobel_v = filters.sobel_v(img_cat)

plt.imshow(img_cat, cmap="Greys_r")
plt.imshow(cat_sobel_h, cmap="Greys_r")
plt.imshow(cat_sobel_v, cmap="Greys_r")

#Aufgabe5.2.2

#imports der noise Bilder
img_n_cat = imread("./catGNoisy.png")
img_n_cat2 = imread("./catGNoisy.png")

#sobel Filter auf noise Bildern
n_cat_sobel_h = filters.sobel_h(img_n_cat)
n_cat_sobel_v = filters.sobel_v(img_n_cat)

plt.imshow(n_cat_sobel_h, cmap="Greys_r")
plt.imshow(n_cat_sobel_v, cmap="Greys_r")

#Gauss Filter auf noise Bild

gaussian_noise_cat = filters.gaussian(img_n_cat2, 5)

gaussian_noise_cat_v = filters.sobel_v(gaussian_noise_cat)
gaussian_noise_cat_h = filters.sobel_h(gaussian_noise_cat)

#Aufgabe5.2.3


plt.show()