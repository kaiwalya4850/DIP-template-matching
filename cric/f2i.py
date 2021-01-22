import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 
import argparse
import glob
import glob

for img in glob.glob("data/*.jpg"):
    image = cv2.imread(img)
    sigma = 0.33
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edges = cv2.Canny(image, lower, upper)
    edges = (255-edges)
    nm = str(img)
    print(nm)
    cv2.imwrite(nm, edges) 