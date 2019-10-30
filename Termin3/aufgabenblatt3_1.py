#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

d = np.load('./trainingsDaten2.npz')
tr_imgs = d['data']
tr_labels = d['labels']

d2 = np.load('./validierungsDaten2.npz')
va_imgs = d2['data']
va_labels = d2['labels']


tr_merkmale = []
va_merkmale = []

for img in tr_imgs:
    tr_merkmale.append(np.mean(img))
    
for img in va_imgs:
    va_merkmale.append(np.mean(img))
    

def euklidDistanz(image_1, image_2):
    return np.sqrt(np.sum((image_1-image_2)**2))

estimated_labels = []
    
for va_img in va_merkmale:
    va_index = 0
    distanzen =  []
    for tr_img in tr_merkmale:
        distanzen.append(euklidDistanz(va_img, tr_img))
    relative_img_index = distanzen.index(np.min(distanzen))
    estimated_labels.append(tr_labels[relative_img_index])
    va_index += 1
        
print(estimated_labels)
print(va_labels)

#verglecihen von estimated und tatsächlich
right_est = 0
 
for index in range(len(va_labels)):
    if va_labels[index] == estimated_labels[index]:
        right_est += 1

trefferquote = (right_est  * 100) / len(estimated_labels)

print(trefferquote)
