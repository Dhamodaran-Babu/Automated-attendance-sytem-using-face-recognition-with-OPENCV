# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:17:35 2020

@author: Dhamodaran
"""

import os ,numpy as np,cv2
from PIL import Image 
import pickle,csv

base_dir=os.path.dirname(os.path.abspath(__file__))
img_dir=os.path.join(base_dir,"images")

label_ids={}
curr_id=1
x_data=[]
y_label=[]


face_detector=cv2.CascadeClassifier(r"C:\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")
face_recognizer=cv2.face.LBPHFaceRecognizer_create()

for root,_dir,files in os.walk(img_dir):
    for file in files:
        if file.endswith("png") or file.endswith("JPG") or file.endswith("jpg"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","_").lower()
            if label not in label_ids:
                label_ids[label]=curr_id
                with open('students details.csv','a')as f:
                    writer=csv.writer(f)
                    writer.writerow([curr_id,label])
                curr_id+=1
                
            id_=label_ids[label]
            img=Image.open(path).convert("L")
            img=np.array(img,"uint8")
            
            faces=face_detector.detectMultiScale(img,scaleFactor=1.05,minSize=(30,30),minNeighbors=5)
            for x,y,w,h in faces:
                roi=img[y:y+h,x:x+w]
        
                x_data.append(roi)
                y_label.append(id_)
                
with open("Dhamodaran_Face_Classifier.pickle",'wb') as f:
    pickle.dump(label_ids,f)         
    
face_recognizer.train(x_data,np.array(y_label))
face_recognizer.save("Dhamodaran_Face_classifier.xml")