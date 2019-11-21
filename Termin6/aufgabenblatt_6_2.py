#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from keras.optimizers import SGD

tr_data = np.load('./trainingsDatenFarbe2.npz')
tr_imgs = tr_data['data']
tr_labels = tr_data['labels']

va_data = np.load('./validierungsDatenFarbe2.npz')
vl_imgs = va_data['data']
vl_labels = va_data['labels']

def euklDist(x,y):
    return np.sqrt(np.sum((x-y)**2))

# Aufgabe 1 

def get_rgb_mws_stds(imgs): # kanalweiser Mittelwert sowie Standardabweichung
    means_r = []
    means_g = []
    means_b = []
    stds_r = []
    stds_g = []
    stds_b = []
    for index in range(len(imgs)):
      img = imgs[index,:,:,:]
      means_r.append(np.mean(img[:,:,0]))
      means_g.append(np.mean(img[:,:,1]))
      means_b.append(np.mean(img[:,:,2]))
      stds_r.append(np.std(img[:,:,0]))
      stds_g.append(np.std(img[:,:,1]))
      stds_b.append(np.std(img[:,:,2]))
      
    return [means_r, means_g, means_b, stds_r, stds_g, stds_b]

#Trainingsdaten berechnen:
tr_rgb_mws_stds = get_rgb_mws_stds(tr_imgs)

#Vlidierungsdaten berechnen:
vl_rgb_mws_stds = get_rgb_mws_stds(vl_imgs)

est_label = []

for i in range(len(vl_imgs)):
    dist = []
    for i2 in range(len(tr_imgs)):
        dist.append(euklDist(vl_imgs_mean[i],tr_imgs_mean[i2]))
    est_label.append(trLabels[dist.index(np.min(dist))])
count = 0
for ind in range(len(est_label)):
    if est_label[ind] == vlLabels[ind]: count += 1

print("Treffer:")
print(count)
print(count/len(vl_imgs)*100, "%")


