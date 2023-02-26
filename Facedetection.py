# Performed using classifier is a algorithm ...which shows whether given image  is negative or positive
# 2 main classifiers are hardcascades and local binary
# like hardcascade to detect upper body, hardcascade to detect smile
# For face detection we will use---hardcascade_fontalface_alt2_xml from opencv github

import cv2 as cv
import numpy as np

img=cv.imread("Faces/group1.jpg")
# cv.imshow("Lady",img)

# face detection doesnt involve looking to skin tone...instead they look towards edges and determine whether it is a face or not
# convert to greyscale 
grayimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",grayimg)

# reading harcascade variable
# it takes first argument of passing path to xml file and stores all 33k lines of code in this variable
haar_cascade=cv.CascadeClassifier('haar_face.xml')
# detectmultiscale will take image use scalefactor and minmum variable to detect face and return a rectangular co-ordiantes of that face as a list to faces on the score rec
# minimum neighb ours is minimum neighbours rectangle should have to be called a face
# minneighbors increases , faces to get detected by cv decreases
faces_rect= haar_cascade.detectMultiScale(grayimg,scaleFactor=1.1,minNeighbors=1)
print(f'Number of faces ={len(faces_rect)}')

# we can loop over the list to grab coordinates of rectangle of image and draw a rectangle over detected faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),thickness=3)
cv.imshow("Detectedface",img)
# it detects 7 images ...coz cascadeclassifier is very sensitive to noise ...therefore we must minimize errors ...sort
# we minimize scale factor in minimum neighbours. So we increase the minumum neighbours to 6 or 7 in group2 image
# some people wearing accesories on face like hat,sunglasses or they arent perpendicular to the camera
cv.waitKey(0)