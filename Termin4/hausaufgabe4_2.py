#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import glob
from skimage.io import imread, imsave
from skimage import measure
import matplotlib.pyplot as plt


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
        mask = img < schwelle
        binarized_images.append(mask.astype(np.int))
    return binarized_images


def crop_images_in_list(image_list, binarized_imgs):
    
    cropped_images = []
    for index,img in enumerate(binarized_imgs):
        props = measure.regionprops(img)[0]
        cropped_images.append(image_list[index][props.bbox[0]:props.bbox[2], props.bbox[1]:props.bbox[3]])
    return cropped_images


train_imgs_names = glob.glob('./haribo1/hariboTrain/*.png')

valid_data = glob.glob('./haribo1/hariboVal/*.png')

tr_imgs = []
tr_labels = []
for image_name in train_imgs_names:
    img = imread(image_name)
    g_img = img[:,:,0]*.33+img[:,:,1]*.33+img[:,:,2]*.33
    tr_imgs.append(g_img)
    tr_labels.append(image_name.split("/")[-1].split(".")[0].split("_")[0])

val_imgs = []
val_labels = []
for img_name in valid_data:
    img = imread(img_name)
    g_img = img[:,:,0]*.33+img[:,:,1]*.33+img[:,:,2]*.33
    val_imgs.append(g_img)
    val_labels.append(img_name.split("/")[-1].split(".")[0].split("_")[0])

bina_tr_imgs = binarize_images_in_list(tr_imgs, 110)
bina_val_imgs = binarize_images_in_list(val_imgs, 110)
cropped_tr_imgs = crop_images_in_list(tr_imgs, bina_tr_imgs)
cropped_val_imgs = crop_images_in_list(val_imgs, bina_val_imgs)

plt.imshow(cropped_val_imgs[10], cmap="Greys_r")


est_labels = []
for cropped_val_imgs in cropped_val_imgs:
    dist = []
    for cropped_tr_imgs in cropped_tr_imgs:
        dist.append(euklDist(rgb_img_to_3d_histo(cropped_val_imgs, bin_count)[0],rgb_img_to_3d_histo(cropped_tr_imgs, bin_count)[0]))
    est_labels.append(tr_labels[dist.index(np.min(dist))])

print_info(est_labels, val_labels)




