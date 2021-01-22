import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 
import numpy as np
import argparse
import glob
import cv2

count = 0
counter = 1

pathOut = "C:/Users/Kaiwalya/Desktop/cric/data/"
vid = "change.mp4"
cap = cv2.VideoCapture(vid)
count = 0
counter += 1
success = True

while success:
    success,image = cap.read()
    print('read a new frame:',success)
    if count%40 == 0 :
        cv2.imwrite(pathOut + 'frame%d.jpg'%count,image)
    count+=1
