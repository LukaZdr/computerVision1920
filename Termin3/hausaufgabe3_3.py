# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import numpy as np

bin_count = 7
d = np.load('./trainingsDatenFarbe2.npz')
trImgs = d['data']
trLabels = d['labels']
trHistos = list(map(lambda x:
                      [
                        np.histogram(x[:,:,0], bins = bin_count, range = (0,256)),
                        np.histogram(x[:,:,1], bins = bin_count, range = (0,256)),
                        np.histogram(x[:,:,2], bins = bin_count, range = (0,256))
                      ], trImgs))

v = np.load('./validierungsDatenFarbe2.npz')
valImgs = v['data']
valLabels = v['labels']
valHistos = list(map(lambda x:
                      [
                        np.histogram(x[:,:,0], bins = bin_count, range = (0,256)),
                        np.histogram(x[:,:,1], bins = bin_count, range = (0,256)),
                        np.histogram(x[:,:,2], bins = bin_count, range = (0,256))
                      ], valImgs))

def eukl_dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def color_histo_nn(va_histos, tr_histos):
  est_label_list = []
  for va_histo in va_histos:
    distances = []
    for tr_histo in tr_histos:
      rgb_distances = []
      for color_dimension in range(3):
        rgb_distances.append(eukl_dist(va_histo[color_dimension][0], tr_histo[color_dimension][0]))
      distances.append(sum(rgb_distances))
    index = distances.index(min(distances))
    est_label_list.append(trLabels[index])
  return est_label_list

est_labels = color_histo_nn(valHistos, trHistos)

print("berechnete Klassifizierung mit Mittelwerten:")
print(est_labels)
print("korrekte Werte:")
print(valLabels)

count = 0
for ind in range(len(est_labels)):
    if est_labels[ind] == valLabels[ind]: count += 1

print("Treffer:")
print(count)

print(count/len(valImgs)*100, "%")

# Die Ergebnisse verbessern sich, die Trefferquote liegt bei 50%
