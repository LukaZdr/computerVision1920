# -*- coding: utf-8 -*-

import numpy as np

# Methoden zum 1d-Farbhistogramme erstellen
def rgb_img_to_1d_histo(img, bin_count):
    img = img.ravel() # ravel => returns flattend 1d-Array
    return np.histogram(img, bins = bin_count, range=(0,256))

def rgb_imgs_to_1d_histos(img_list, bin_count):
    return list(map(lambda img: rgb_img_to_1d_histo(img, bin_count), img_list))

def eukl_dist(x,y):
		return np.sqrt(np.sum((x-y)**2))

def rgb_img_mean(img):
	return np.mean(np.array(img[:,:,2]))

def indices_of_n_smallest_values(n, num_list):
	return np.array(num_list).argsort()[:n]

def elements_for_index_list(index_list, elements_list):
	return list(map(lambda x: elements_list[x], index_list))

def most_common_occurrence(element_list):
	return max(element_list,key=element_list.count)

def calculate_combined_weighted_distanze(image_1, weight, image_2):
	distance_1 = eukl_dist(rgb_img_mean(image_1),
												 rgb_img_mean(image_2))
	distance_2 = eukl_dist(rgb_img_to_1d_histo(image_1, bin_count)[0],
												 rgb_img_to_1d_histo(image_2, bin_count)[0])
	return distance_1 + weight * distance_2

def color_histo_n_nearest_neighbour(va_imgs, tr_imgs, neighbour_count):
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

def guessing_accuracy(est_labels, va_labels):
	# print("berechnete Klassifizierung mit Mittelwerten:")
	# print(est_labels)
	# print("korrekte Werte:")
	# print(va_labels)

	count = 0
	for ind in range(len(est_labels)):
			if est_labels[ind] == va_labels[ind]: count += 1

	# print("Treffer:")
	# print(count)
	print('////////////////////////////////////')
	print('bin_count:', bin_count)
	print('neighbours', count_neighbour)
	print('weight:', weight)
	print(count/len(va_imgs)*100, "%")
	return count/len(va_imgs)*100

# Params
# Bilder laden und vorbereiten

# bin_count = 9
# count_neighbour = 7
# weight = 0
d = np.load('./trainingsDatenFarbe2.npz')
tr_imgs = d['data']
tr_labels = d['labels']

v = np.load('./validierungsDatenFarbe2.npz')
va_imgs = v['data']
va_labels = v['labels']

neighbours = [3, 5, 10]
ahhhh = []
for bin_count in range(2,11):
	print(bin_count)
	for count_neighbour in range(2,10):
		for weight in [0]:

			#Ausfuehren der Auswertung
			est_labels = color_histo_n_nearest_neighbour(va_imgs, tr_imgs, count_neighbour)

			# Statistik
			ahhhh.append(guessing_accuracy(est_labels, va_labels))

print(max(ahhhh))

# bin_count: 6
# neighbours 5
# weight: 0.1
# 66.66666666666666 %