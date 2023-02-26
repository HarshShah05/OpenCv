import cv2 as cv
# to rescale a video 
# 0.75 means ki utne se chota hoga video frame
def rescalevideo(frame,scale=0.1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    
    dimensions=(width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def rescalevideo1(frame,scale=0.3):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


capture=cv.VideoCapture('Videos/Video1.mp4')
while True:
    isTrue,frame=capture.read()
    resize_vid=rescalevideo(frame)
    # resize_vid2=rescalevideo1(frame)
    # cv.imshow('video',resize_vid2)
    cv.imshow('video',resize_vid)
    
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()







