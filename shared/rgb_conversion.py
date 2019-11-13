import numpy as np

def to_1d_histo(img):
	img = img.ravel() # ravel => returns flattend 1d-Array
	return np.histogram(img, bins = bin_count, range=(0,256))

def to_3d_histo(img):
	img =  img.reshape((img.shape[0]*img.shape[1],3))
	return np.histogramdd(img, bins = [bin_count,bin_count,bin_count], range=((0,256),(0,256),(0,256)))

def to_mean(img): # der Farbmittelwert eines Bildes
	return np.mean(img, axis = (0,1,2))
