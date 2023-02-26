import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
# 255--white color
# blank.copy()--temporary modifies the blank not permanently
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,thickness=-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)



# Bitwise and---will take both images and place it over one another and give intersection


bitand=cv.bitwise_and(rectangle,circle)
cv.imshow("And",bitand)


# Bitwise or 

bitor=cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitor)


# bitwise xor---return non intersecting regions
# inverts the bits---ie it changed black to white and white to black
# bitxor=cv.bitwise_xor(rectangle)
# cv.imshow("xor",bitxor)

bitnot=cv.bitwise_not(rectangle,circle)
cv.imshow("not",bitnot)
# if we subtract bitwise xor form bitwise or we get bitwise and

cv.waitKey(0)