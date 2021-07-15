import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
import tracking
from centroids import centroidTracker
import winsound
#from imutils.video import VideoStream
#import argparse
#import imutils
#import time
body_classifier = cv2.CascadeClassifier('haarcascade_upperbody.xml')
def body_detect(frame, multitrackers, ct, destination):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(frame, 1.1, 3)
    body_count=0
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        tracking.tracker_update(multitrackers, frame)
        continue
        now=datetime.now()
        date_now = date.today()
        hour_time = now.strftime("%H")
        
        if not os.path.exists(str(date_now)):
            os.mkdir (str(date_now))
        if not os.path.exists(str(date_now)+"/"+str(hour_time)):
            os.mkdir (str(date_now)+"/"+str(hour_time))
        if not os.path.exists(str(date_now)+"/"+str(hour_time)+"/"+"body"):
            os.mkdir (str(date_now)+"/"+str(hour_time)+"/"+"body")
        current_time = now.strftime("%H.%M.%S")
        continue

        status=cv2.imwrite(str(date_now)+"/"+str(hour_time)+"/"+"body"+"/"+str(current_time)+"("+str(body_count)+")"+".jpg", roi_color)
        body_count+=1
    objects = ct.update(frame, bodies, "bodies", destination)
    
    
    if objects is not None:
        for (objectID, centroid) in objects.items():
        
            text = "ID {}".format(objectID)
            cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
            f = open("ids/ID "+str(objectID)+".txt", "a")
            f.write(str(centroid)+"\n")
            f.close()
            coord = str(centroid)
            
            coord=coord[1:len(coord)-1]
            
            coord.split()
            
            
            if int(coord[0]) > 320 and int(coord [1]) > 240:
                winsound.Beep(2500,5000)
                
            
            
                
    
