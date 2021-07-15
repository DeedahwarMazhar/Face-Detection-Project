import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
from imutils.video import VideoStream
import argparse
import imutils
#from imutils import FPS
import time
import accessCam






def trackers_ini():
    
    return cv2.MultiTracker_create()

###############################################################################################################


def tracker_update(multitrackers, frame):
    OPENCV_OBJECT_TRACKERS = {
        
	"kcf": cv2.TrackerKCF_create
    }
    (success, boxes) = multitrackers.update(frame)
    
    for box in boxes:
	    (x, y, w, h) = [int(v) for v in box]
	    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	    roi_color = frame[y:y+h, x:x+w]
	    tracker = OPENCV_OBJECT_TRACKERS[args["kcf"]]()
	    multitrackers.add(tracker, frame, box)
    
    
    
    

