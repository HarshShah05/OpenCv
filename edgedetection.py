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
cv.waitKey(0)