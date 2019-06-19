import os
import cv2
import pickle
import numpy as np
from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, '')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


def detectFace(name, path):
    labels = name.split('.')
    
    label = labels[0]
    i = os.path.join(path, name)
    x = os.path.basename(i)
    img = cv2.imread(x)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
            
    for (x, y, width, height) in faces:
        img = cv2.rectangle(img, (x, y),(x+width, y+height), (255,0,0), 2)
        eye_gray = gray[y: y+height, x: x+width]
        face_color = img[y: y+height, x: x+width]

        eyes = eye_cascade.detectMultiScale(eye_gray)
    
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
     
        font = cv2.FONT_HERSHEY_COMPLEX
        color = (255,255,255)
        stroke =2
        cv2.putText(img, label,(x,y), font,1, color, stroke, cv2.LINE_AA )


    cv2.imshow('Image with face detection', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



print('Following pics are present: ')
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
            path = os.path.join(root, file)
            label = os.path.basename(path)
            print(label)


name = input('Enter image name: ')
print(root)
detectFace(name, root)
            