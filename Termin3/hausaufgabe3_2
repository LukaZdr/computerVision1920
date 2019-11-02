# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import numpy as np

d = np.load('./trainingsDatenFarbe2.npz')
trImgs = d['data']
trLabels = d['labels']

v = np.load('./validierungsDatenFarbe2.npz')
valImgs = v['data']
valLabels = v['labels']

def euklDist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def calcVals(Imgs, meanList):
    for index in range(len(Imgs)):
        img = Imgs[index,:,:,:]
        meanList.append(np.array([np.mean(img[:,:,0]),np.mean(img[:,:,1]),np.mean(img[:,:,2])]))
    
#Trainingsdaten berechnen:
trImgs_mean = []
calcVals(trImgs, trImgs_mean)

#Validierungsdaten berechnen:
valImgs_mean = []
calcVals(valImgs, valImgs_mean)

est_label = []

for i in range(len(valImgs)):
    dist = []
    for i2 in range(len(trImgs)):
        dist.append(euklDist(valImgs_mean[i],trImgs_mean[i2]))
    est_label.append(trLabels[dist.index(np.min(dist))])
    
print("berechnete Klassifizierung mit Mittelwerten:")
print(est_label)
print("korrekte Werte:")
print(valLabels)
    
count = 0
for ind in range(len(est_label)):
    if est_label[ind] == valLabels[ind]: count += 1
    
print("Treffer:")
print(count)
print(count/len(valImgs)*100, "%")

# Die Ergebnisse verbessern sich, die Trefferquote liegt bei 50%
