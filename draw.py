import cv2 as cv
import numpy as np

# creating a blank image
# height,widht,no of_color channels
blank =np.zeros((1000,1000,3),dtype='uint8')
# cv.imshow("Blank",blank)

# Painting an image
# blank[:]==covering all pixels

# blank[:]=0,255,255
# cv.imshow("Yellow",blank)




# Only a portion of entire blank image
# blank[200:300,300:400]=255,255,0
# cv.imshow("White",blank)








# 2--Draw a empty rectangle  inside it
# 0,0 is origin that is takes point as a argument
# cv.rectangle(blank,(0,0),(250,350),(0,255,0),thickness=2)


# # 2.2----Draw a filled rectangle 
# cv.rectangle(blank,(0,0),(250,350),(0,255,0),thickness=-1)
# cv.imshow("rectangle",blank)








# 3--Draw a circle
# check arguments by hovering over the cv.circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),50,(255,255,255),thickness=5)
# cv.imshow("Circle",blank)
# cv.waitKey(0)


# 4--Draw a line
# # (250,250) is the lenght of line
# (0,0) is from where line starts off
# cv.line(blank,(0,0),(250,250),(0,0,255),thickness=2)
# cv.imshow("Line",blank)






# Text on image
# (0,255)ie starts from 0 to 255
cv.putText(blank,"Harsh Shah",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
cv.imshow("Text",blank)
cv.waitKey(0)