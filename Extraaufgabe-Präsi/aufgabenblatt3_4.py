# -*- coding: utf-8 -*-

import numpy as np

# Methoden zum 1d-Farbhistogramme erstellen
def rgb_img_to_1d_histo(img, bin_count): # nimmt ein bild und macht es zu einem 1d histogramm
    img = img.ravel() # ravel => returns flattend 1d-Array
    return np.histogram(img, bins = bin_count, range=(0,256))

def eukl_dist(x,y): 
		return np.sqrt(np.sum((x-y)**2))

def rgb_img_mean(img): # der farb mittelwert eines bildes
	return np.mean(img[:,:,2])
	# return np.mean(img)

def indices_of_n_smallest_values(n, num_list): # gibt die indizes der n kleinsten elemente des arrays zurueck
	return np.array(num_list).argsort()[:n]

def elements_for_index_list(index_list, elements_list): # gibt fuer eine liste an indizes und eine an elementen die elemente der indizes zurueck
	return list(map(lambda x: elements_list[x], index_list))

def most_common_occurrence(element_list): # gibt das am oeften auftretende element zurueck
	return max(element_list,key=element_list.count)

def calculate_combined_weighted_distanze(image_1, weight, image_2): # nimmt die euklidische distanz von dem mittelwert und histogrammen und summiert sie gewichtet auf
	distance_1 = eukl_dist(rgb_img_mean(image_1),
												 rgb_img_mean(image_2))
	#mit 3d histogrammen
	# image_1 =  image_1.reshape((image_1.shape[0]*image_1.shape[1],3))
	# image_2 =  image_2.reshape((image_2.shape[0]*image_2.shape[1],3))
	# distance_2 = eukl_dist(np.histogramdd(image_1, bins = [8,8,8], range=((0,256),(0,256),(0,256)))[0],
	# 											 np.histogramdd(image_2, bins = [8,8,8], range=((0,256),(0,256),(0,256)))[0])
	
	# mit 2d histogrammen										
	distance_2 = eukl_dist(rgb_img_to_1d_histo(image_1, bin_count)[0],
												 rgb_img_to_1d_histo(image_2, bin_count)[0])
	return distance_1 + weight * distance_2

def rgb_img_n_nearest_neighbour(va_imgs, tr_imgs, neighbour_count): # brechnet durch die n naechsten nachbarn das warcheinliche label
	# guard clause wenn neighborcount hoeher ist als die liste
	est_labels_list = []
	for va_img in va_imgs:
		distances = []
		for tr_img in tr_imgs:
			distance = calculate_combined_weighted_distanze(va_img, weight, tr_img)
			distances.append(distance)
		index_list = indices_of_n_smallest_values(neighbour_count, distances)
		n_closest_labels = elements_for_index_list(index_list, tr_labels)
		est_label = most_common_occurrence(n_closest_labels)
		est_labels_list.append(est_label)
	return est_labels_list

def guessing_accuracy(est_labels, va_labels): # Wirft auf der console infos aus und retuned genauigkeit in %

	count = 0
	for ind in range(len(est_labels)):
			if est_labels[ind] == va_labels[ind]: count += 1
	# fuer das checken auf der console 
	print('////////////////////////////////////')
	print('bin_count:', bin_count)
	print('neighbours', count_neighbour)
	print('weight:', weight)
	print(count/len(va_imgs)*100, "%")

	# rueckgabe wert = accuracy in %
	return count/len(va_imgs)*100

# Params
bin_count = 6
count_neighbour = 5
weight = 0.1

# Bilder laden und vorbereiten
d = np.load('./trainingsDatenFarbe2.npz')
tr_imgs = d['data']
tr_labels = d['labels']

v = np.load('./validierungsDatenFarbe2.npz')
va_imgs = v['data']
va_labels = v['labels']

#Ausfuehren der Auswertung
est_labels = rgb_img_n_nearest_neighbour(va_imgs, tr_imgs, count_neighbour)

# Statistik
print(guessing_accuracy(est_labels, va_labels))


# bin_count: 6
# neighbours 5
# weight: 0.1
# 66.66666666666666 %