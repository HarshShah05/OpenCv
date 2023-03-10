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
    cv.imwrite("Q2-A.jpg",img1)
elif str==2:
  b2=int(input("Enter height"))
  a2=int(input("Enter width"))
  blank =np.ones((b2,a2,3),dtype='uint8')
  blank[:]=255,255,255
  def option2(blank):
    cv.line(blank,(0,0),(a2,0),(0,0,0),100)
    cv.line(blank,(0,0),(0,b2),(0,0,0),100)
    cv.line(blank,(0,b2),(a2,b2),(0,0,0),100)
    cv.line(blank,(a2,0),(a2,b2),(0,0,0),100)
    cv.line(blank,(100,100),(900,100),(0,0,0),50)
    cv.line(blank,(100,100),(100,400),(0,0,0),50)
    cv.line(blank,(100,400),(900,400),(0,0,0),50)
    cv.line(blank,(900,100),(900,400),(0,0,0),50)
    return (blank)
  
  img2=option2(blank)
  cv.imshow("option2",img2)
  cv.imwrite("Q2-B.jpg",blank)
  cv.waitKey(0)
  
    
    
elif str==3:
    a1=int(input("Enter first dimension: "))
    b1=int(input("Enter second dimension: "))
    color=[]
    blank=np.ones((b1,a1,3),dtype="uint8")
    blank[:]=255,255,255
    d1=int(input("Enter number of boxes :"))
    for i in range(1,d1+1):
      ci=input(f"Enter color of box {i} in lowercase ")
      color.append(ci)
    if color[0]=="red":
      c1=(0,0,255)
    elif color[0]=="green":
      c1=(0,255,0)
    elif color[0]=="yellow":
      c1=(0,255,255)
    else:
      c1=(255,0,0)
      
    # 2nd box
    if color[1]=="red":
            c2=(0,0,255)
    elif color[1]=="green":
          c2=(0,255,0)
    elif color[1]=="yellow":
          c1=(0,255,255)
    else:
          c2=(255,0,0)
      
    # 3rd box
    if color[2]=="red":
        c3=(0,0,255)
    elif color[2]=="green":
      c3=(0,255,0)
    elif color[2]=="yellow":
      c3=(0,255,255)
    else:
          c3=(255,0,0)
      
    # 4th box 
    if color[3]=="red":
          c4=(0,0,255)
    elif color[3]=="green":
        c4=(0,255,0)
    elif color[3]=="yellow":
       c4=(0,255,255)
    else:
       c4=(255,0,0)
    
    def option3(blank):
      cv.rectangle(blank,(0,0),(a1//2,b1//2),(c1),thickness=-1)
      cv.rectangle(blank,(a1//2,0),(a1,b1//2),(c2),thickness=-1)
      cv.rectangle(blank,(0,b1//2),(a1//2,b1),(c3),thickness=-1)
      cv.rectangle(blank,(a1//2,b1//2),(a1,b1),(c4),thickness=-1)
      return (blank)
    img3=option3(blank)
    cv.imshow("Option 3",img3)
    cv.waitKey(0)
    cv.imwrite("Que2-c.jpg",img3)
    
else:
  print("Plz enter among the 3 options only")

red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)
yellow=(0,255,255)
black=(0,0,0)