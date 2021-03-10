import numpy as np
import cv2 as cv

# save np.load
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

people = ['Ben Affleck', 'Jerry', 'Salman']

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = np.load('features.npy')
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\Pratik\Pictures\Face Detection\Val\ben.jfif')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)

#Detect faces
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with a confidence = {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0),thickness=2)
cv.imshow('Recognised Image', img)
cv.waitKey(0)