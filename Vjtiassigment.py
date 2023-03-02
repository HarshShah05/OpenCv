import cv2 as cv
import numpy as np

# a=int(input("Enter dimension 1 "))
# b=int(input("Enter dimension 2 "))
blank =np.ones((1000,1000,3),dtype='uint8')
blank[:]=255,255,255
# cv.imshow("Blank",blank)

cv.rectangle(blank,(100,100),(0,0),((0,0,255)),thickness=-1)
cv.rectangle(blank,(1000,0),(1000,100),((0,255,255)),thickness=-1)
# cv.imshow("blank",blank)



#cv.putText(blank,"VJTI",(70,120),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
cv.imshow("Text",blank)
cv.imwrite('bl.jpg',blank)
cv.waitKey(0)


