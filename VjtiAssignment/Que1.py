import cv2 as cv
import numpy as np


a=int(input("Enter dimension 1 "))
b=int(input("Enter dimension 2 "))
blank =np.ones((b,a,3),dtype='uint8')
blank[:]=255,255,255
# cv.imshow("Blank",blank)


red=(0,0,255)
yellow=(0,255,255)
green=(0,255,0)
blue=(255,0,0)
lightblue=(255,255,0)
black=(0,0,0)
white=(255,255,255)

cv.rectangle(blank,(0,0),(100,100),((red)),thickness=-1)
cv.rectangle(blank,((a-100),0),(a,100),((yellow)),thickness=-1)
cv.rectangle(blank,(0,(b-100)),(100,b),((green)),thickness=-1)
cv.rectangle(blank,((a-100),(b-100)),(a,b),((blue)),thickness=-1)

# Centte box
cv.rectangle(blank,(550,400),(950,600),((lightblue)),thickness=-1)
# cv.rectangle(blank,(750-200,500-100),(750+200,500+100),((0,255,0)),thickness=-1)

cv.putText(blank,"VJTI",(710,510),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
cv.imshow("Question1",blank)
cv.imwrite("question1.jpg",blank)
cv.waitKey(0)