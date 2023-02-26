import cv2 as cv
import numpy as np

img=cv.imread("Pics/flower2.jpg")

# Grayscale
# Blur
# edge cascade
#crop
# dilated
# erorded




# Grayscale
def resizeimg(img):
    width=int(img.shape[1]/5)
    height=int(img.shape[1]/5)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("Smaller image",reimg)

 
# Converting image to greyscale
bimg=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Grey",bimg)


# Blur
# (3,3)--- k-size:it needs to be an odd number---more the size more the blur effect
blur=cv.GaussianBlur(reimg,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)


# edge cascade
eimg=cv.Canny(blur,125,175)
cv.imshow("Edge",eimg)


# cropping
# we do slicing for it
cimg=img[100:400,300:400]
cv.imshow("Cropped",cimg)
cv.waitKey(0)