#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imsave
img = imread("./cat.png")
r_img = img[:,:,0]
g_img = img[:,:,1]
b_img = img[:,:,2]
plt.imshow(r_img, cmap="Greys_r")
plt.show()

# Aufgabe 1.3
"""
Beim Ausgeben der Bilder sieht man, dass um so mehr Anteil des jeweiligen Kanals an einem Pixel vohanden ist
desto heller wirkt der Pixel.
Haben wir also einen weißen Pixel, der im aditiven Farbsystem aus allen farben besteht, sollte er in allen Kanälen weiß erscheinen.
Analog dazu sollte ein schwarzer Pixel, der im aditivem Farbsystem die Abszinenz von allen drei Farben darstellt, auch in allen Kanälen schwarz erscheinen.
"""

# Aufgabe 1.4
strange_cat = np.dstack((b_img, g_img, r_img))
plt.imshow(strange_cat)
plt.show()

"""
Da die einzenen Kanäle nur durch ihre Position im  Bild-Array die Information beinhalten welche Farbintensität sie wiederspiegeln, sind sie sür sich gesehen nur eine Darstellung von Farbintensität einer anonymen Farbe. Packt man also das Bild-Array in der falschen reihenfolge wieder zusammen werden einfach die Farbintensitätslisten vertauscht und die Katze die schön warm und orange wirkte ist jetzt in einem Kalten blau zu sehen.
"""

# Aufgabe 1.5
plt.imshow(255-img)
plt.show()
"""
Es wird die gegentilige Farbe im rgb-Würfel gesucht und anstelle dieses Pixels gesetzt.
"""

# Aufabe 1.6
"""
Es kann das 3D-Bild-Array zu einem 2D-Array umgeformt werden indem man die rgb-Achen einfach hintereinander in eine Dimension schreibt und von dieser dann einen Mittelwert oder ein Histogramm bildet.
"""