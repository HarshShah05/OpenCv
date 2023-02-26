
import cv2 as cv
import numpy as np

img=cv.imread("Pics/tree.jpg")
def resizeimg(img):
    width=int(img.shape[1]/7)
    height=int(img.shape[1]/9)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)



reimg=resizeimg(img)
grayimg=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Tree",reimg)
# simple thresholding--pass grayscale image 
# it compares each pixel value to this threshold value(150)...if its above this..then turns them to 255 ....if falls below it then to 0
# more the number less white will be displayed
threshold,thresh=cv.threshold(grayimg,175,255,cv.THRESH_BINARY)
# cv.imshow("Threshimg1",thresh)



threshold,thresh_inv=cv.threshold(grayimg,175,255,cv.THRESH_BINARY_INV)
# cv.imshow("Threshimg2",thresh_inv)


# adaptive threshold---computer finds good value by itself by defining a block size or kernel size ie 11
# finds itself the value of max thresh

adaptive_thresh=cv.adaptiveThreshold(grayimg,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Adaptive thresh",adaptive_thresh)
cv.waitKey(0)