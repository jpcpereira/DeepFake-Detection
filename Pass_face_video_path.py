
#!pip install opencv-python==3.3.0.9

#!pip install cv2

#!python -V


#!python -m pip install --upgrade pip

#!pip install cv2
#!pip install opencv-python
#!pip install mtcnn
#!pip install tensorflow
#!pip install tensorflow==2.0.0-beta0
#!pip install -U numpy

import cv2
import mtcnn
from mtcnn.mtcnn import MTCNN
import numpy as np
import pandas as pd
import math
import os
import sys
import h5py

detector = MTCNN()

#Function for passing
def find_processed_faces(v_path):
    n_frames = 11
    video = cv2.VideoCapture(v_path)
    print(video.isOpened())
    framerate = video.get(5)
    count=1
    frameindex=1
    try:
        while (video.isOpened()):
            frameId = video.get(1)
            #print()
            success, image = video.read()
            if( image is not None ):
                result = detector.detect_faces(image)
                if(len(result)>1):
                    max_area = 0
                    max_idx = -1
                    idx=0
                    for i in range(len(result)):
                        bounding_box = result[i]['box']
                        area=abs((bounding_box[1]-(bounding_box[1] + bounding_box[3]))*(bounding_box[0]-(bounding_box[0]+bounding_box[2])))
                        #print(area)
                        if area>max_area:
                            max_area=area
                            max_idx=i
                       #idx=idx+1
                    #print(max_area)
                    #print(max_idx)
                    bounding_box = result[max_idx]['box']
                    crop_img = image[(bounding_box[1]-28):(bounding_box[1]-28 + bounding_box[3]+56), (bounding_box[0]-28):(bounding_box[0]-28+bounding_box[2]+56)]

                else:
                    bounding_box = result[0]['box']
                    keypoints = result[0]['keypoints']
                ##Creating rectangle
                    cv2.rectangle(image,
                              (bounding_box[0]-25, bounding_box[1]-25),
                              (bounding_box[0]-25+bounding_box[2]+50, bounding_box[1]-25 + bounding_box[3]+50),
                              (0,155,255),2)
                ##Cropping the images

                    crop_img = image[(bounding_box[1]-28):(bounding_box[1]-28 + bounding_box[3]+56), (bounding_box[0]-28):(bounding_box[0]-28+bounding_box[2]+56)]


                # print(crop_img.size())
                crop_img = cv2.resize(crop_img, (152,179), interpolation = cv2.INTER_AREA)
            if (success != True):
                print("Break1")
                break
            if (frameId % math.floor(framerate) == 0):
                destn_path="C:\\Users\\Administrator\\Desktop\\hackathon\\faces\\"+v_path.split("\\")[-1].replace(".mp4","")
                os.mkdir(destn_path)
                filename=destn_path+"\\image_" + str(int(frameId / math.floor(framerate))+1) + ".jpg"
                cv2.imwrite(filename,crop_img)
                frameindex=frameindex+1
            count=count+1
            if frameindex==n_frames:
                print("Break2")
                break
        return (True,filename)
    except:
        return (False,"")
