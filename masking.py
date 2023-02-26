# masking helps us to focus on certain parts of image we would like to focus on like face of people only

import numpy as np
import cv2 as cv

img=cv.imread("Pics/sungirl.jpg")
def resizeimg(img):
    width=int(img.shape[1]/10)
    height=int(img.shape[1]/10)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("sungirl",reimg)

# The masking can be done by a blank image only if the dimensions are same
blank=np.zeros(reimg.shape[:2],dtype='uint8')
mask=cv.circle(blank,(reimg.shape[1]//2,reimg.shape[0]//2),100,(255,255,255),-1)
maskedimage=cv.bitwise_and(reimg,reimg,mask=mask)
cv.imshow("masked",mask)
cv.imshow("Maskedimg",maskedimage)
cv.waitKey(0)