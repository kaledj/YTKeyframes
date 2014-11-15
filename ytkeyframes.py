import cv2, sys
import numpy as np
from download import Download
from boundarydetector import BoundaryDetector
from kfextractor import KeyframeExtractor

url = "http://www.youtube.com/watch?v=6FDTMRK7-24"

def main():
	print("Downloading video...")
	url = sys.argv[1]
	dl = Download(url)
	videoFile = dl.getVideo()
	# videoFile = "testVideo.mp4"

	print("Detecting shot boundaries...")
	bd = BoundaryDetector(videoFile)
	shotBounds = bd.getShotBoundaries()
	print("{0} shot boundaries found...".format(np.sum(shotBounds)))
	# shotBounds = np.load("bounds.npy")

	print("Extracting representative keyframes...")
	kfExtractor = KeyframeExtractor(videoFile)
	frames = kfExtractor.extractKeyframes(shotBounds)
	for frame in frames:
		cv2.imshow("Keyframes", frame)
		cv2.waitKey()   

if __name__ == '__main__':
	main()