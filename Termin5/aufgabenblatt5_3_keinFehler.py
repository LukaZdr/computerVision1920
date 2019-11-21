#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import feature

img_cat = imread('./catG.png')
img_eye = imread('./catEye.png')

#Aufgabe 2 + 3
img_matched = feature.match_template(img_cat, img_eye, pad_input=True)
x, y = np.unravel_index(np.argmax(img_matched), img_matched.shape)

plt.imshow(img_matched)
plt.show()

print("Gefundener Bereich: X=" + str(x) + ", Y=" + str(y))



#Aufgabe 5
img_background = imread('./whereIsWally1.jpg')
img_wally = imread('./wally.png')

img_matched_wally = feature.match_template(img_background, img_wally, pad_input=True)

#plt.imshow(img_background)
#plt.show()

x_wally, y_wally = np.unravel_index(np.argmax(img_matched_wally), (img_matched_wally.shape[0], img_matched_wally.shape[1]))

plt.imshow(img_matched_wally)
plt.show()

print("Wally: Gefundener Bereich: X=" + str(x_wally) + ", Y=" + str(y_wally))


#Aufgabe 6
# Weil das Gesicht von Wally auf der Briefmarke viel zu groß ist und so für den Computer eklatant anders aussieht als die Mini-Version die zum Suchen verwendet wird (?)
