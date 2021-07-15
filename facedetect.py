import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
import tracking
from centroids import centroidTracker
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detect(frame, multitrackers, ct, destination):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    face_count=0
    for (x,y,w,h) in faces:
         
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         #roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]
         tracking.tracker_update(multitrackers, frame)
         
        ############################################################################################################################
         #eyes = eye_cascade.detectMultiScale(roi_gray)
         #for (ex,ey,ew,eh) in eyes:
             #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         continue
         now=datetime.now()
         date_now = date.today()
         hour_time = now.strftime("%H")
         #path="C:/Users/Deedahwar/Desktop/camera"+str(date_now)
         if not os.path.exists(str(date_now)):
            os.mkdir (str(date_now))
         if not os.path.exists(str(date_now)+"/"+str(hour_time)):
            os.mkdir (str(date_now)+"/"+str(hour_time))
         if not os.path.exists(str(date_now)+"/"+str(hour_time)+"/"+"faces"):
            os.mkdir (str(date_now)+"/"+str(hour_time)+"/"+"faces")
           
        
         current_time = now.strftime("%H.%M.%S")
         #print(str(current_time))
         
         #img = "%s/%s/%s %s:%s:%s_(%s).jpg"%(now.month, now.day, now.year, now.hour, now.minute, now.second, face_count)
         status=cv2.imwrite(str(date_now)+"/"+str(hour_time)+"/"+"faces"+"/"+str(current_time)+"("+str(face_count)+")"+".jpg", roi_color)
         face_count+=1

    #return faces

    objects = ct.update(frame, faces, "faces", destination)
    if objects is not None:
         for (objectID, centroid) in objects.items():
            
            text = "ID {}".format(objectID)
            cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
            #cv2.imwrite("a.jpg",)











            
         #video, associated with frame
         #track
         #sfe, kalman filtering
         #human detection, frontal
         #save_face
         #draw path
         
         


#+"/"+str(hour_time)

