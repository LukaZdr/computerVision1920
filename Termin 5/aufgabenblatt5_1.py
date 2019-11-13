#import
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
img = imread("./catGNoisy.png")
plt.imshow(img, cmap="Greys_r")


#implement
def faltung(img):
  soft_img = []
  for x in range(1,len(img)-1):
    soft_img.append([])
    for y in range(1,len(img[0])-1):
      pix_list = []
      pix_list.append(img[x-1][y-1])
      pix_list.append(img[x-1][y])
      pix_list.append(img[x-1][y+1])
      pix_list.append(img[x][y-1])
      pix_list.append(img[x][y])
      pix_list.append(img[x][y+1])
      pix_list.append(img[x+1][y-1])
      pix_list.append(img[x+1][y])
      pix_list.append(img[x+1][y+1])
      soft_img[x-1].append(np.mean(pix_list))
  return soft_img
print(np.shape(img))
print(np.shape(faltung(img)))
plt.imshow(faltung(img), cmap="Greys_r")