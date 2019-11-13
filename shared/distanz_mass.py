import numpy as np

def eukl_dist(x,y):
		return np.sqrt(np.sum((x-y)**2))

def intersection(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection
