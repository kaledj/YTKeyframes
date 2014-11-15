from pytube import YouTube
from pprint import pprint
import sys
import cv2
import os


# name = (str(yt.filename) + ".mp4")
# print name
# vidfile = cv2.VideoCapture(name)
# cv2.namedWindow("Current frame")
# ret, currFrame = vidfile.read()

# while(ret):
#     cv2.imshow("Current frame", currFrame)
#     ret, currFrame = vidfile.read()
#     key = cv2.waitKey(33)
#     if key is 113: 
#         break


class Download(object):
    def __init__(self,url):
        self.url = url
        yt = YouTube()
        video = yt.get('mp4', '480p')
        video = yt.get('mp4')
        video.download()
        self.name = (str(yt.filename) + ".mp4")

    def getVideo(self):
        return self.name

    def __del__(self):
        os.remove(self.name)