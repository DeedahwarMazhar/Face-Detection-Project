import cv2
import numpy as np
import os
from datetime import datetime
import time
from datetime import date
from PIL import Image
import facedetect
import accessCam
import centroids
import tracking
import bodydetect
import plot

choice=input("Choose your mode:\n1.Webcam\n2.External Camera\n3.Video File \n")
if choice=="1":
    
    accessCam.access_camera(0)
if choice=="2":
    accessCam.access_camera(1)
if choice=="3":
    while True:
        mode=input("Enter the name of your file.\nWARNING: FILE MUST BE IN THE VIDEOS FOLDER OF THE ROOT DIRECTORY.")
        if not os.path.isfile("videos/"+mode+'.avi'):
            print("File not found")
            print(" ")
        else:
            accessCam.access_camera("videos/"+mode+".avi")
            break

choice_2=input("Which ID do you want to plot?\n ")
plot.plot_file(choice_2)


print("CIAO")
