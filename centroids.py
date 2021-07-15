from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2
import os
from datetime import datetime
from datetime import date


class centroidTracker:

    def __init__(self, maxDisappeared=50):
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()
        self.maxDisappeared = maxDisappeared



    def register(self, centroid, frame, mode, destination):
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1
        now=datetime.now()
        date_now = date.today()
        hour_time = now.strftime("%H")
        if not os.path.exists(destination+"/"+str(date_now)):
            os.mkdir (destination+"/"+str(date_now))
        if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)):
            os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time))
        if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode):
            os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode)
        
        if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1)):
            os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1))

        status=cv2.imwrite(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1)+"/"+str(now.strftime("%H.%M.%S")+".jpg"),frame)
        f = open("ids/ID "+str(self.nextObjectID-1)+".txt", "w")
        f.write(str(centroid)+"\n")
        f.close()
            



    def deregister(self, objectID):
        del self.objects[objectID]
        del self.disappeared[objectID]





    def update(self, frame, rects, mode, destination):
            
        if len(rects) == 0:
                
               for objectID in list(self.disappeared.keys()):

                   self.disappeared[objectID] += 1    
                   
               
               

                    
                   if self.disappeared[objectID] > self.maxDisappeared:
                       self.deregister(objectID)



               return self.objects



        inputCentroids = np.zeros((len(rects), 2), dtype="int")
        
        for (i, (startX, startY, endX, endY)) in enumerate(rects):
            
            # use the bounding box coordinates to derive the centroid
            cX = int((startX + endX) /1.15)
            cY = int((startY + endY) /1.15)
            inputCentroids[i] =  (cX, cY)
            #make frame
            roi_color=frame[startY:startY+endY, startX:startX+endX]
            

        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                   self.register(inputCentroids[i], roi_color, mode, destination)


        else:
                
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.values())

            D = dist.cdist(np.array(objectCentroids), inputCentroids)

            rows = D.min(axis=1).argsort()

            cols = D.argmin(axis=1)[rows]


            usedRows = set()
            usedCols = set()
            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)


            for (row, col) in zip(rows, cols):

                      if row in usedRows or col in usedCols:
                          continue
                      objectID = objectIDs[row]
                      self.objects[objectID] = inputCentroids[col]
                      self.disappeared[objectID] = 0



                      now=datetime.now()
                      date_now = date.today()
                      hour_time = now.strftime("%H")
                      if not os.path.exists(destination+"/"+str(date_now)):
                          os.mkdir (destination+"/"+str(date_now))
                      if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)):
                        os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time))
                      if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode):
                          os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode)
                    
                      if not os.path.exists(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1)):
                          os.mkdir (destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1))

                      status=cv2.imwrite(destination+"/"+str(date_now)+"/"+str(hour_time)+"/"+mode+"/"+str(self.nextObjectID-1)+"/"+str(now.strftime("%H.%M.%S")+".jpg"),roi_color)


                      usedRows.add(row)
                      usedCols.add(col)

                      if D.shape[0] >= D.shape[1]:  
            

            

                          for row in unusedRows:

                              
                              objectID = objectIDs[row]
                              try:
                                  self.disappeared[objectID] += 1
                              except KeyError:
                                  continue
                                  

                              

                              if self.disappeared[objectID] > self.maxDisappeared:

                                  self.deregister(objectID)

                      else:
                          for col in unusedCols:

                              
                              self.register(inputCentroids[col], roi_color, mode, destination)
                                  

                              
            return self.objects
                    


          


        





                









            
    
