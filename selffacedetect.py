import cv2 as cv
import numpy as np
# Facedetection
video=cv.VideoCapture(0)
xmlread=cv.CascadeClassifier('haar_face.xml')
while True:
    ret,frame=video.read()
    facedetect=xmlread.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in facedetect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),thickness=2)
    cv.imshow("Frame",frame)
    k=cv.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv.destroyAllWindows()
    
