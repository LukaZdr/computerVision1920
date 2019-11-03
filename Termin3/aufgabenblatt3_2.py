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


tr_histos = list(map(lambda x: np.histogram(x, bins = 15, range = (0,256)), tr_imgs))
va_histos = list(map(lambda x: np.histogram(x, bins = 15, range = (0,256)), va_imgs))


def euklidDistanzHisto(histo_1, histo_2):
    return np.sqrt(np.sum((histo_1[0]-histo_2[0])**2))

estimated_labels = []

for va_histo in va_histos:
    distanzen =  []
    for tr_histo in tr_histos:
        distanzen.append(euklidDistanzHisto(va_histo, tr_histo))
    relative_img_index = distanzen.index(np.min(distanzen))
    print(np.min(distanzen))
    estimated_labels.append(tr_labels[relative_img_index])

#verglecihen von estimated und tatsächlich
right_est = 0

for index in range(len(va_labels)):
    if va_labels[index] == estimated_labels[index]:
        right_est += 1

trefferquote = (right_est  * 100) / len(estimated_labels)

print(trefferquote)
