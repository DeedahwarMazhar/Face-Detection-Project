import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detect(frame_cam):
    gray = cv2.cvtColor(frame_cam, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
         
         cv2.rectangle(frame_cam,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame_cam[y:y+h, x:x+w]
         eyes = eye_cascade.detectMultiScale(roi_gray)
         #for (ex,ey,ew,eh) in eyes:
             #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         now=datetime.now()
         date_now = date.today()
         hour_time = now.strftime("%H")
         #path="C:/Users/Deedahwar/Desktop/camera"+str(date_now)
         if not os.path.exists(str(date_now)+"/"+str(hour_time)):
            os.mkdir (str(date_now)+"/"+str(hour_time))
         current_time = now.strftime("%H.%M.%S")
         #print(str(current_time))
         
         #img = "%s/%s/%s %s:%s:%s_(%s).jpg"%(now.month, now.day, now.year, now.hour, now.minute, now.second, face_count)
         status=cv2.imwrite(str(date_now)+"/"+str(hour_time)+"/"+"{}.jpg".format(current_time), roi_color)
         

now=datetime.now()    
hour_time = now.strftime("%H")
face_detect()

