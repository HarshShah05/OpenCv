import cv2 as cv
import numpy as np

# contours are basically boundries of object 

img=cv.imread("Pics/Water.jpg")

def resizeimg(img):
    width=int(img.shape[1]/10)
    height=int(img.shape[1]/20)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)

reimg=resizeimg(img)
cv.imshow("Water",reimg)

graywaterimage=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",graywaterimage)

blur=cv.GaussianBlur(reimg,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)


cannimgage=cv.Canny(blur,125,150)
cv.imshow("Canned",cannimgage)
# contours returns 2 things
# contours and heirachy
# cv.retertree is mode in which it finds contours and returns all heirachical contours, cv.chain...approamition method
# from 2500+ now its only 183
# contours, hierarchy= cv.findContours( cannimgage,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# print(len(contours))


# threshing binarizes a image ie 0 or black or white or 255
ret,thresh=cv.threshold(graywaterimage,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)
cv.waitKey(0)