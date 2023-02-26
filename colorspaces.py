import cv2 as cv
import numpy as np

img=cv.imread("Pics/Indiagate.jpg")

def resizeimg(img):
    width=int(img.shape[1]/3)
    height=int(img.shape[1]/5)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("Img",reimg)

graygate=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Graygate",graygate)

# Converting to HSV

hsvimg=cv.cvtColor(reimg,cv.COLOR_BGR2HSV)
cv.imshow("Hsvimage",hsvimg)

# Converting to lab

labimg=cv.cvtColor(reimg,cv.COLOR_BGR2LAB)
cv.imshow("Labimg",labimg)

# Converting bgr to rgb
# open cv by default takes BGR images but its actually RGB in real sense ...we can check through matplotlib

rgbimg=cv.cvtColor(reimg,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgbimg)
cv.waitKey(0)