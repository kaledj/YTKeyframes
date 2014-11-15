import cv2, tools, sys
import numpy as np

class BoundaryDetector(object):
	def __init__(self, videoFile):
		self.videoFile = videoFile

	def getShotBoundaries(self):
		# Load video and initialize variables
		vidCap = cv2.VideoCapture(self.videoFile)
		nFrames = vidCap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
		ret, frame = vidCap.read()
		prev = frame.copy()
		prevFrameDist = currFrameDist = 0

		time = 0
		shotBounds = np.zeros(nFrames, dtype=bool)
		while ret:
			prevHist = tools.getColorHist(prev)
			currHist = tools.getColorHist(frame)
			prevFrameDist = currFrameDist
			currFrameDist = tools.compareHist(prevHist, currHist)
			
			if (prevFrameDist * 10) < currFrameDist and \
			   (prevFrameDist + 10000) < currFrameDist:
				shotBounds[time] = 1 

			prev = frame.copy()
			ret, frame = vidCap.read()
			time += 1
			# key = cv2.waitKey(33)
			# if key == 27: break
		vidCap.release()
		return shotBounds
