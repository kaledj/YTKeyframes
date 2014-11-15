__author__ = 'smithc4'
import numpy as np

def block_average(video, length, width):
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

def frame_average(length, width):



