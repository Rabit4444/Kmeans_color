# import the necessary packages
import numpy as np
import cv2
def centroid_histogram(labels):
	#lay so luong cum
	numLabels = np.arange(0, len(np.unique(labels)) + 1)
	#tinh toan bieu do 1 tap hop du lieu,bins- xac dinh so mau tren bieu do
	(hist, _) = np.histogram(labels, bins = numLabels)
	# chuan hoa du lieu va dua chung ve cung 1 bieu do
	hist = hist.astype("float")
	hist /= hist.sum()

	return hist
def plot_colors(hist, centroids):
	#tao hcn 50x300 pixel bo sung khong gian cho mau RGB
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0

	for (percent, color) in zip(hist, centroids):
		#tinh % tung mau trong bieu do
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
			color.astype("uint8").tolist(), -1)
		startX = endX

	return bar