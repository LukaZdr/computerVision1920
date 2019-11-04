#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

label_names = {
        1: "auto",
        4: "hirsch",
        8: "schiff"}

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
    estimated_labels.append(tr_labels[relative_img_index])

#verglecihen von estimated und tatsächlich
right_est = 0

for index in range(len(va_labels)):
    if va_labels[index] == estimated_labels[index]:
        right_est += 1




trefferquote = (right_est  * 100) / len(estimated_labels)

print(trefferquote)

def make_confusion_matrix(est_values, actual_values):
    table_content = {
        "auto": {
            "auto": 0,
            "hirsch": 0,
            "schiff": 0
            },
        "hirsch": {
            "auto": 0,
            "hirsch": 0,
            "schiff": 0
            },
        "schiff": {
            "auto": 0,
            "hirsch": 0,
            "schiff": 0
            }
        }
    for index, est_value in enumerate(est_values):
        table_content[label_names[est_value]][label_names[actual_values[index]]] += 1
    return table_content

print(make_confusion_matrix(estimated_labels, va_labels))

"""
Unser Ergebniss ist ein 2D-Dict in dem die erste Schicht die richtigen Labels sind und die zweite Schicht die erratenen Labels.
Heist der Aufruf:

ergebnis_2d_dict[4][8]
>>> 5

bedeutet das beim label 4 fuenf mal das Label 8 geraten wurde
"""