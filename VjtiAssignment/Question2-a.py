import cv2 as cv
import numpy as np
# RGB code for colors

red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)
yellow=(0,255,255)
black=(0,0,0)


str=int(input("Type option number from 3 options: "))
if str==1:
    a=int(input("Enter height: "))
    b=int(input("Enter width: "))
    blank =np.ones((a,b,3),dtype="uint8")*255
    c=int(input("Enter thickness of line: "))
    d=int(input("Enter no of horizantal lines: "))
    e=int(input("Enter no of vertical lines: "))

    def lines(blank):
    # Horizantal lines
       cv.line(blank,(0,(a//5)),(b,(a//5)),(black),thickness=c)
       cv.line(blank,(0,(2*a//5)),(b,(2*a//5)),(black),thickness=c)
       cv.line(blank,(0,(3*a//5)),(b,(3*a//5)),(black),thickness=c)
       cv.line(blank,(0,(4*a//5)),(b,(4*a//5)),(black),thickness=c)
       # Vertical lines
       cv.line(blank,(200,0),(200,a),(0,0,0),thickness=c)
       cv.line(blank,(390,0),(390,a),(0,0,0),thickness=c)
       cv.line(blank,(570,0),(570,a),(0,0,0),thickness=c)
       cv.line(blank,(740,0),(740,a),(0,0,0),thickness=c)
       return (blank)

    img1=lines(blank)
    cv.imshow("Blank",img1)
    cv.waitKey(0)
    cv.imwrite("Lines.jpg",img1)
    
    
elif str==3:
    a1=int(input("Enter first dimension: "))
    b1=int(input("Enter second dimension: "))
    c1=int(input("Enter no of boxes:"))
    blank=np.ones((b1,a1,3),dtype="uint8")
    blank[:]=255,255,255
    def option3(blank):
        
      cv.rectangle(blank,(0,0),(a1//2,b1//2),(red),thickness=-1)
      cv.rectangle(blank,(a1//2,0),(a1,b1//2),(green),thickness=-1)
      cv.rectangle(blank,(0,b1//2),(a1//2,b1),(blue),thickness=-1)
      cv.rectangle(blank,(a1//2,b1//2),(a1,b1),(yellow),thickness=-1)
      return (blank)
    img2=option3(blank)
    cv.imshow("Option 3",img2)
    cv.waitKey(0)
    cv.imwrite("Microsoft.jpg",img2)
    
    

