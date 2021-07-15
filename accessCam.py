import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
import tracking
from centroids import centroidTracker
import facedetect
import bodydetect
import imutils

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

def access_camera(mode):
    if mode==1:
        destination="webcam"
    if mode==2:
        destination="external camera"
    if mode!=1 and mode!=2:
        destination="videotests"

    ct = centroidTracker()
    (H, W) = (None, None)
   
    
    cv2.namedWindow("preview")
    start=datetime.now()
    
    hour_time = start.strftime("%H")

    date_now = date.today()

    face_count=0
    vid_count=0
    #if mode == 2 or mode==1:
    

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    while os.path.isfile("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi'):
                vid_count+=1
    out = cv2.VideoWriter("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi', fourcc, 20.0, (640,480))
    

    #car
    vc = cv2.VideoCapture(mode)
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')
    date_now = date.today()
    #out = cv2.VideoWriter(str(date_now)+'/output.avi', fourcc, 20.0, (640,480))
    
    face_count=0
    vid_count=0
    
    multitrackers=tracking.trackers_ini()
    
    if vc.isOpened(): # try to get the first frame
        
        rval, frame = vc.read()
        
        #while os.path.isfile("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi'):
                #vid_count+=1
        #out = cv2.VideoWriter("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi', fourcc, 20.0, (640,480))
    else:
        rval = False

    while rval:
        frame = cv2.flip(frame,1)
        #if mode == 2 or mode ==1:
        out.write(frame)
        cv2.imshow("preview", frame)
        rval, frame = vc.read()

        #frame = frame[1] if mode != 0 and mode != 1 else frame

        if frame is None:
            break
	   

        #frame = imutils.resize(frame, width=600)

        if W is None or H is None:
            (H, W) = frame.shape[:2]

        
        #call facerecog
        #faces=
        #facedetect.face_detect(frame, multitrackers, ct, destination)
        #objects = ct.update(faces)
        
        #objects=[]

        
        bodydetect.body_detect(frame, multitrackers, ct, destination)
        
        #break
        current=datetime.now()
        current_hour=current.strftime("%H")
        if mode == 2 or mode == 1:
            if current_hour != hour_time:
                while os.path.isfile("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi'):
                    vid_count+=1
                    
                #out = cv2.VideoWriter("videos/"+str(date_now)+" hour:"+str(hour_time)+"("+str(vid_count)+")"+'.avi', fourcc, 20.0, (640,480))
                #vc.release()
                    
                out.write()
                out.release()
                hour_time=current_hour
                continue
        key = cv2.waitKey(20)
        if key == 27:
            #while os.path.isfile("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi'):
                #vid_count+=1
            #out = cv2.VideoWriter("videos/"+str(date_now)+" hour"+str(hour_time)+"("+str(vid_count)+")"+'.avi', fourcc, 20.0, (640,480))
            #if mode == 2 or mode==1:
            vc.release()
            out.release()
            break
    cv2.destroyWindow("preview")

#access_camera(0)

    
