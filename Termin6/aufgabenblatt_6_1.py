#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bilderGenerator
import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1

tr_mws, tr_stds, tr_labels = bilderGenerator.zieheBilder(500)
vl_mws, vl_stds, vl_labels = bilderGenerator.zieheBilder(50)

# Aufgabe 2

plt.close('all')

tr_pos_indexes = np.where(tr_labels == 1)
tr_mws_pos = tr_mws[tr_pos_indexes]
tr_stds_pos = tr_stds[tr_pos_indexes]
plt.plot(tr_mws_pos,tr_stds_pos,'rx')

tr_neg_indexes = np.where(tr_labels == -1)
tr_mws_neg = tr_mws[tr_neg_indexes]
tr_stds_neg = tr_stds[tr_neg_indexes]
plt.plot(tr_mws_neg,tr_stds_neg,'bx')

# plt.show()

# Aufgabe 3

w1 = 0.0001
w2 = -0.0002
b = 0.001

est_list = []
for index in range(len(vl_labels)):
  y = w1 * vl_mws[index] + w2 * vl_stds[index] + b
  if y >= 0:
    est_list.append(1)
  else:
    est_list.append(-1)

hits = 0
for index in range(len(est_list)):
  if est_list[index] == vl_labels[index]:
    hits += 1

print(hits/len(vl_labels))

# Aufgabe 4

w1 = 0.0001
w2 = -0.0002
b = 0.001
learn_rate=0.0000005

for index in range(len(tr_labels)):
    y= w1 * tr_mws[index] + w2*tr_stds[index] + b
    if np.sign(y) != np.sign(tr_labels[index]):
        # Variablen beladen
        temp_w1_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_mws[index]
        temp_w2_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_stds[index]
        temp_b_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index])
        w1 = w1 - learn_rate * temp_w1_neu
        w2 = w2 - learn_rate * temp_w2_neu
        b = b - learn_rate * temp_b_neu

est_list = []
for index in range(len(vl_labels)):
  y = w1 * vl_mws[index] + w2 * vl_stds[index] + b
  if y >= 0:
    est_list.append(1)
  else:
    est_list.append(-1)


hits = 0
for index in range(len(vl_labels)):
    if est_list[index] == vl_labels[index] :
        hits += 1

print((hits/len(vl_labels)))

# Aufgabe 5

w1 = np.random.normal(0,0.001)
w2 = np.random.normal(0,0.001)
b = 0
learn_rate=0.0000005

for index in range(len(tr_labels)):
    y= w1 * tr_mws[index] + w2*tr_stds[index] + b
    if np.sign(y) != np.sign(tr_labels[index]):
        # Variablen beladen
        temp_w1_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_mws[index]
        temp_w2_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_stds[index]
        temp_b_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index])
        w1 = w1 - learn_rate * temp_w1_neu
        w2 = w2 - learn_rate * temp_w2_neu
        b = b - learn_rate * temp_b_neu

est_list = []
for index in range(len(vl_labels)):
  y = w1 * vl_mws[index] + w2 * vl_stds[index] + b
  if y >= 0:
    est_list.append(1)
  else:
    est_list.append(-1)


hits = 0
for index in range(len(vl_labels)):
    if est_list[index] == vl_labels[index] :
        hits += 1

print((hits/len(vl_labels)))

""" Trotz random generiertem startwert ist die genauigkeit immer 98%"""

# Aufgabe 6

w1 = np.random.normal(0,0.001)
w2 = np.random.normal(0,0.001)
b = 0
learn_rate=0.0000005
epochs = 100

for epoch in range(epochs):
  for index in range(len(tr_labels)):
      y = w1 * tr_mws[index] + w2 * tr_stds[index] + b
      if np.sign(y) != np.sign(tr_labels[index]):
          # Variablen beladen
          temp_w1_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_mws[index]
          temp_w2_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index]) * tr_stds[index]
          temp_b_neu = 2*(w1 * tr_mws[index] + w2 * tr_stds[index] + b - tr_labels[index])
          w1 = w1 - learn_rate * temp_w1_neu
          w2 = w2 - learn_rate * temp_w2_neu
          b = b - learn_rate * temp_b_neu

  est_list = []
  for index in range(len(vl_labels)):
    y=w1 *vl_mws[index] + w2*vl_stds[index] + b
    if y >= 0:
      est_list.append(1)
    else:
      est_list.append(-1)


  hits = 0
  for index in range(len(vl_labels)):
      if est_list[index] == vl_labels[index]:
          hits += 1
print((hits/len(vl_labels)))

"""beide varianten haben eine Genauigkteit die, in den Itterationen zwischen 100% und 98% schwankt, die Genauigkeit hat aber eine starke tendenz zu 100%"""

# Aufgabe 7

x_values = []
y_values = []

for x in range(255):
  for y in range(128):
    y_near = w1 * x + w2 * y + b
    if y_near < 0.0001:
      x_values.append(x)
      y_values.append(y)

plt.plot(x_values, y_values, 'yx')

plt.show()