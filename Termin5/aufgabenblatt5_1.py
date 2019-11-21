#import
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
img = imread("./catGNoisy.png")
plt.imshow(img, cmap="Greys_r")

#implement
def faltung(img):
  bildMitRahmen = np.zeros((img.shape[0]+2, img.shape[1]+2))
  bildMitRahmen[1:-1, 1:-1] = img
  soft_img = []
  for x in range(1,len(bildMitRahmen)-1):
    soft_img.append([])
    for y in range(1,len(bildMitRahmen[0])-1):
      pix_list = []
      pix_list.append(bildMitRahmen[x-1][y-1])
      pix_list.append(bildMitRahmen[x-1][y])
      pix_list.append(bildMitRahmen[x-1][y+1])
      pix_list.append(bildMitRahmen[x][y-1])
      pix_list.append(bildMitRahmen[x][y])
      pix_list.append(bildMitRahmen[x][y+1])
      pix_list.append(bildMitRahmen[x+1][y-1])
      pix_list.append(bildMitRahmen[x+1][y])
      pix_list.append(bildMitRahmen[x+1][y+1])
      soft_img[x-1].append(np.mean(pix_list))
  return soft_img

plt.imshow(faltung(img), cmap="Greys_r")
plt.show()