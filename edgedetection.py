# Lpalacian image seems like a image drawn over blackboard with chalk duster

import numpy as np
import cv2 as cv

img=cv.imread("Pics/tower.jpg")

def resizeimg(img):
    width=int(img.shape[1]/5)
    height=int(img.shape[1]/5)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)

reimg=resizeimg(img)
cv.imshow("Tower",reimg)

grayimg=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Black",grayimg)

# Laplacian
lap =cv.Laplacian(grayimg,cv.CV_64F)
# all pixels values are converted to absolute values...UInt8 is image dtype
lap=np.uint8(np.absolute(lap))

# Canny

cannyimg=cv.Canny(grayimg,150,175)
cv.imshow("Cannyimg",cannyimg)
cv.imshow('Laplacian',lap)
cv.waitKey(0)