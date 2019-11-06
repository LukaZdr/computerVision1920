#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import glob
from skimage.io import imread, imsave

train_imgs_names = glob.glob('./haribo1/hariboTrain/*.png')

valid_data = glob.glob('./haribo1/hariboVal/*.png')

tr_imgs = []
tr_labels = []
for image_name in train_imgs_names:
    tr_imgs.append(imread(image_name))
    tr_labels.append(image_name.split("/")[-1].split(".")[0].split("_")[0])


val_imgs = []
val_labels = []
for img_name in valid_data:
    val_imgs.append(imread(img_name))
    val_labels.append(img_name.split("/")[-1].split(".")[0].split("_")[0])
    
def print_info(est_labels, val_labels):
    print("berechnete Klassifizierung:")
    print(est_labels)
    print("korrekte Werte:")
    print(val_labels)
    
    count = 0
    for ind in range(len(est_labels)):
        if est_labels[ind] == val_labels[ind]: count += 1
    
    print("Treffer:")
    print(count)
    print(count/len(val_imgs)*100, "%")
    
def euklDist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def calcVals(imgs, meanList):
    for img in imgs:
        meanList.append(np.array([np.mean(img[:,:,0]),np.mean(img[:,:,1]),np.mean(img[:,:,2])]))
        

#Trainingsdaten berechnen:
trImgs_mean = []
calcVals(tr_imgs, trImgs_mean)

#Validierungsdaten berechnen:
valImgs_mean = []
calcVals(val_imgs, valImgs_mean)


est_labels = []

for i in range(len(val_imgs)):
    dist = []
    for i2 in range(len(tr_imgs)):
        dist.append(euklDist(valImgs_mean[i],trImgs_mean[i2]))
    est_labels.append(tr_labels[dist.index(np.min(dist))])

print_info(est_labels, val_labels)

#Aufgabe 1.3

bin_count = 8
def rgb_img_to_3d_histo(img, bin_count):
	img =  img.reshape((img.shape[0]*img.shape[1],3))
	return np.histogramdd(img, bins = [bin_count,bin_count,bin_count], range=((0,256),(0,256),(0,256)))

est_labels = []
for val_img in val_imgs:
    dist = []
    for tr_img in tr_imgs:
        dist.append(euklDist(rgb_img_to_3d_histo(val_img, bin_count)[0],rgb_img_to_3d_histo(tr_img, bin_count)[0]))
    est_labels.append(tr_labels[dist.index(np.min(dist))])

print_info(est_labels, val_labels)
    

