__author__ = 'smithc4'
import numpy as np
import cv2

def blockAverage(video, length, width):
    len_block = length / 4;
    width_block = width / 4;
    len_block2 = len_block * 2;
    len_block3 = len_block * 3;
    width_block2 = width_block * 2;
    width_block3 = width_block * 3;
    top_left = np.average(np.average(video[0:len_block][0:width_block]))
    topmid_left = np.average(np.average(video[0:len_block][width_block:width_block2]))
    bottommid_left = np.average(np.average(video[0:len_block][width_block2:width_block3]))
    bottom_left = np.average(np.average(video[0:len_block][width_block3:width]))

def frameAverage(length, width):
    pass

def getColorHist(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.calcHist([frame], [0], None, [256], [0, 256])

def compareHist(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.cv.CV_COMP_CHISQR)

