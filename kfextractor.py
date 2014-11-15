import cv2, tools
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans

class KeyframeExtractor(object):
	def __init__(self, videoFile):
		self.videoFile = videoFile
		self.keyframes = []

	def extractKeyframes(self, shotBoundaries):
		print("Extracting keyframes")
		vidCap = cv2.VideoCapture(self.videoFile)
		ret, frame = vidCap.read()
		nFrames = vidCap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
		self.frameHistFeats = np.zeros((nFrames, 256))
		time = 0
		while ret:
			if shotBoundaries[time]:
				# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				self.keyframes.append(frame)
			self.frameHistFeats[time] = tools.getColorHist(frame).ravel()
			ret, frame = vidCap.read()
			time += 1
		vidCap.release()
		return self.removeRedundantFrames()

	def removeRedundantFrames(self):
		h, w, d = self.keyframes[0].shape
		n = len(self.keyframes)
		frames = np.zeros((n, 256))
		self.frameHistFeats
		for i, kf in enumerate(self.keyframes):
			frames[i] = tools.getColorHist(kf).ravel()
		
		k = int(np.sqrt(n))
		kmeans = KMeans(k)
		print("Clustering frames into {0} code vectors.".format(k))
		kmeans.fit(self.frameHistFeats)

		bestFrameIndices = []
		bestFrames = []
		NN = NearestNeighbors(1)
		NN.fit(frames)
		centers = kmeans.cluster_centers_
		for center in centers:
			nearest = NN.kneighbors(center, return_distance=False)
			bestFrameIndices.append(nearest[0])
		bestFrameIndices.sort()
		for i in bestFrameIndices:
			bestFrames.append(self.keyframes[i])
		return bestFrames
