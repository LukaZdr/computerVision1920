#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from skimage.io import imread, imsave
img_1 = imread("./agri3.png")
img_2 = imread("./agri6.png")

mean_img_1 = np.mean(img_1)
mean_img_2 = np.mean(img_2)

mean_diff = np.absolute(mean_img_1 - mean_img_2)

print(mean_diff)

