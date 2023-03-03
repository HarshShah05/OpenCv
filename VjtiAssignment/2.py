import cv2 as cv 
import numpy as np    

b2=int(input("Enter height"))
a2=int(input("Enter width"))

blank =np.ones((b2,a2,3),dtype='uint8')
blank[:]=255,255,255
cv.line(blank,(0,0),(a2,0),(0,0,0),100)
cv.line(blank,(0,0),(0,b2),(0,0,0),100)
cv.line(blank,(0,b2),(a2,b2),(0,0,0),100)
cv.line(blank,(a2,0),(a2,b2),(0,0,0),100)



# Inner lines
cv.line(blank,(100,100),(900,100),(0,0,0),50)
cv.line(blank,(100,100),(100,400),(0,0,0),50)
cv.line(blank,(100,400),(900,400),(0,0,0),50)
cv.line(blank,(900,100),(900,400),(0,0,0),50)




cv.imshow("option2",blank)
cv.imwrite("opt2.jpg",blank)
cv.waitKey(0)