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

def tracking(frame, roi_color):
    trackerType = "CSRT"
    multiTracker = cv2.MultiTracker_create()
    for bbox in bboxes:
        multitracker.add(createTrackerByName(trackerType), frame, bbox)

