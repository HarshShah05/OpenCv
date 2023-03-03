import cv2 as cv
import numpy as np


a=int(input("Enter first dimension: "))
b=int(input("Enter second dimension: "))
blank=np.ones((b,a,3),dtype="uint8")
blank[:]=255,255,255
# cv.imshow("Microsoft_logo",blank)

red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)
yellow=(0,255,255)



cv.rectangle(blank,(0,0),(a//2,b//2),(red),thickness=-1)
cv.rectangle(blank,(a//2,0),(a,b//2),(green),thickness=-1)
cv.rectangle(blank,(0,b//2),(a//2,b),(blue),thickness=-1)
cv.rectangle(blank,(a//2,b//2),(a,b),(yellow),thickness=-1)


cv.imshow("Blank",blank)
cv.imwrite("Microsoft.jpg",blank)

cv.waitKey(0)