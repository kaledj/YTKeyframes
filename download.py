from pytube import YouTube
from pprint import pprint
import sys
import cv2
import os

class Download(object):
    def __init__(self,url):
        self.url = url
        yt = YouTube()
        yt.url = url
        video = yt.get('mp4', '480p')
        video = yt.get('mp4')
        video.download()
        self.name = (str(yt.filename) + ".mp4")

    def getVideo(self):
        return self.name

    def __del__(self):
        os.remove(self.name)