# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 16:54:52 2020

@author: Dhamodaran
"""

import cv2,time
import pickle
import mark_attendace

# I request eveeryone to read the readme file more clearly to understand how to run these codes.
#Hope You achieve what you are aiming for..Best wishes from Dhamodaran..Thank you..

print("\t\t WELCOME TO DHAMO'S LIVE FACE DETECTOR")
print("\t\t\t...Hope you will be gettng caught:)")

label_ids={}
with open("Dhamodaran_Face_Classifier.pickle",'rb') as f:
    org=pickle.load(f) 
    label_ids={v:k for k,v in org.items()}
    
face_detector=cv2.CascadeClassifier(r"C:\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")

face_recognizer=cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(r"Dhamodaran_Face_classifier.xml")

video=cv2.VideoCapture(0)
count=0

while True:
    count+=1
    check,frame=video.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(gray,scaleFactor=1.05,minSize=(40,30),minNeighbors=8,flags=cv2.CASCADE_SCALE_IMAGE)
    for x,y,w,h in faces:
        roi_gray=gray[y:y+h,x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        id_,conf=face_recognizer.predict(roi_gray)
        if conf>72:
            cv2.putText(frame,label_ids[id_],(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(230,230,230),1,cv2.LINE_AA)
            mark_attendace.attendance_marker(id_)
            #cv2.putText(frame,conf,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(230,230,230),1,cv2.LINE_AA)
    cv2.imshow("Live Face Detector",frame)
    if cv2.waitKey(1)==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
print("Total Frames recorded",count)
print("FACE DETECTION SESSION SUCCESSFULL")
time.sleep(3)