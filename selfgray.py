import cv2 as cv
video=cv.VideoCapture(0)




def change_res(width, height):
    video.set(3, width)
    video.set(4, height)
    
change_res(2000, 720)


while True:
    ret,frame=video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # cv.imshow("Frame",frame)
    cv.imshow("Gray",gray)
    
    k=cv.waitKey(1)
    if k==ord('q'):
        break

video.read()
cv.destroyAllWindows()