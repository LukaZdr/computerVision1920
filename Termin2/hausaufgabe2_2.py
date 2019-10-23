#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from skimage.io import imread, imsave

def eukl_dis(img_1, img_2):
    bin_count = 8
    
    histo_1 = np.histogram(img_1, bins=bin_count, range =(0,256))
    histo_2 = np.histogram(img_2, bins=bin_count, range =(0,256))
    
    summe = 0
    for index in range(bin_count-1):
        diff =  histo_1[0][index-1]-histo_2[0][index-1]
        summe += np.absolute(diff)**2
    return np.sqrt(summe)

img_1 = imread("./agri3.png")
img_2 = imread("./agri6.png")

print(eukl_dis(img_1, img_2))