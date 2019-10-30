# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import numpy as np
import matplotlib.pyplot as plt

d = np.load('./trainingsDaten2.npz')
trImgs = d['data']
trLabels = d['labels']

v = np.load('./validierungsDaten2.npz')
valImgs = v['data']
valLabels = v['labels']

def euklDist(x,y):
    return np.sqrt(np.sum((x-y)**2))

bin_count = 15

def calcVals(Imgs, meanList, histoList):
    for index in range(len(Imgs)):
        img = Imgs[index,:,:]
        meanList.append(np.mean(img)) # Mittelwert
        histoList.append(np.histogram(img, bins=bin_count, range =(0,256)))
    
#Trainingsdaten berechnen:
trImgs_mean = []
trImgs_histo = []
calcVals(trImgs, trImgs_mean, trImgs_histo)

#Validierungsdaten berechnen:
valImgs_mean = []
valImgs_histo = []
calcVals(valImgs, valImgs_mean, valImgs_histo)

est_label = []
est_label_histo = []
for i in range(len(valImgs)):
    dist = []
    histo_dist = []
    for i2 in range(len(trImgs)):
        dist.append(np.absolute(valImgs_mean[i]-trImgs_mean[i2]))
        histo_dist.append(euklDist(valImgs_histo[i][0],trImgs_histo[i2][0]))
    est_label.append(trLabels[dist.index(np.min(dist))])
    est_label_histo.append(trLabels[histo_dist.index(np.min(histo_dist))])
    
print("berechnete Klassifizierung mit Mittelwerten:")
print(est_label)
print("korrekte Werte:")
print(valLabels)
    
count = 0
for ind in range(len(est_label)):
    if est_label[ind] == valLabels[ind]: count += 1
    
print("Treffer:")
print(count)

print("mit histogrammen klassifiziert:")
print(est_label_histo)

count2 = 0
for ind in range(len(est_label_histo)):
    if est_label_histo[ind] == valLabels[ind]: count2 += 1

print("Treffer:")
print(count2)
