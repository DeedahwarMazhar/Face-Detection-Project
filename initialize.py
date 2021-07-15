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
from imutils import FPS
import time
import accessCam

def track_ini():
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create
    }
    return cv2.MultiTracker_create()
    
    
    
    
    

