import cv2

class BoundaryDetector(object):
	def __init__(self, videoFile):
		self.vidCapture = cv2.videoCapture(videoFile)

	def getShotBoundaries(self):

	def __del__(self):
		self.vidCapture.release()
		