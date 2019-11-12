# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:35:53 2019
@author: Christian
"""

import numpy as np
import glob
from skimage.io import imread
from skimage import measure
import matplotlib.pyplot as plt
from skimage import filters
from skimage import transform

def print_info(est_labels, val_labels):
    print("berechnete Klassifizierung:")
    print(est_labels)
    print("korrekte Werte:")
    print(val_labels)
    
    count = 0
    for ind in range(len(est_labels)):
        if est_labels[ind] == val_labels[ind]: count += 1
    
    print("Treffer:")
    print(count)
    print(count/len(val_imgs)*100, "%")
    
def euklDist(x,y):
    return np.sqrt(np.sum((x-y)**2))

bin_count = 8
def rgb_img_to_3d_histo(img, bin_count):
	img =  img.reshape((img.shape[0]*img.shape[1],3))
	return np.histogramdd(img, bins = [bin_count,bin_count,bin_count], range=((0,256),(0,256),(0,256)))


def binarize_images_in_list(image_list, schwelle):
    binarized_images = []
    for img in image_list:
        #ohne OTSU:
        #mask = img < schwelle
        
        #OTSU:
        schwelle_otsu = filters.threshold_otsu(img)
        mask = img < schwelle_otsu
        #print(schwelle_otsu)
        binarized_images.append(mask.astype(np.int))
    return binarized_images

bla = []

def crop_images_in_list(image_list, binarized_imgs):
    cropped_images = []
    for index,img in enumerate(binarized_imgs):
        rotated_mask = transform.rotate(img, 0, order=0, preserve_range=True)
        rotated_img =  transform.rotate(image_list[index], 0, order=0)
        
        
        
        coordinates_foreground_pixel = np.where(rotated_mask == 1)
        
        bla.append(coordinates_foreground_pixel)
        
        min_x = np.amin(coordinates_foreground_pixel[0])
        max_x = np.amax(coordinates_foreground_pixel[0])         
        min_y = np.amin(coordinates_foreground_pixel[1])
        max_y = np.amax(coordinates_foreground_pixel[1])
        
        #props = measure.regionprops(rotated_mask)[0]
        cropped_images.append(rotated_img[min_x:max_x, min_y:max_y])
    return cropped_images


train_imgs_names = glob.glob('./haribo1/hariboTrain/*.png')

valid_data = glob.glob('./haribo1/hariboVal/*.png')

tr_imgs = []
tr_labels = []
tr_imgs_color = []
for image_name in train_imgs_names:
    img = imread(image_name)
    g_img = img[:,:,0]*.33+img[:,:,1]*.33+img[:,:,2]*.33
    tr_imgs.append(g_img)
    tr_imgs_color.append(img)
    tr_labels.append(image_name.split("\\")[-1].split(".")[0].split("_")[0])
                   

val_imgs = []
val_labels = []
val_imgs_color = []
for img_name in valid_data:
    img = imread(img_name)
    g_img = img[:,:,0]*.33+img[:,:,1]*.33+img[:,:,2]*.33
    val_imgs.append(g_img)
    val_imgs_color.append(img)
    val_labels.append(img_name.split("\\")[-1].split(".")[0].split("_")[0])

bina_tr_imgs = binarize_images_in_list(tr_imgs, 110)
bina_val_imgs = binarize_images_in_list(val_imgs, 110)
cropped_tr_imgs = crop_images_in_list(tr_imgs, bina_tr_imgs)
cropped_val_imgs = crop_images_in_list(val_imgs, bina_val_imgs)

cropped_tr_imgs_color = crop_images_in_list(tr_imgs_color, bina_tr_imgs)
cropped_val_imgs_color = crop_images_in_list(val_imgs_color, bina_val_imgs)
 

#plt.imshow(cropped_tr_imgs_color[4])

#show all images
for img in cropped_val_imgs_color:
    plt.imshow(img)
    plt.show()
    
for img in cropped_tr_imgs_color:
    plt.imshow(img)
    plt.show()


est_labels = []
for val_img in cropped_val_imgs_color:
    dist = []
    for tr_img in cropped_tr_imgs_color:
        dist.append(euklDist(rgb_img_to_3d_histo(val_img, bin_count)[0],rgb_img_to_3d_histo(tr_img, bin_count)[0]))
    est_labels.append(tr_labels[dist.index(np.min(dist))])

print_info(est_labels, val_labels)

"""
OTSU:
    
filters.threshold_otsu(image)
"""

"""
zu Aufgabe 2.2:
Ergebnis mit 3D-Histogramm und selbst ausprobiertem Schwellenwert(110): 91.66666666666666 %
zu Aufgabe 2.3:
Die Ergebnisse sind gleich gut geblieben: 91.66666666666666 %
"""