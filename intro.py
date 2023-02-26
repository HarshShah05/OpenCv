# reading images
import cv2 as cv
fimg=cv.imread('Pics/flower2.jpg')


# # takes 2 parameters  one is window name and second pixels o display...which is img
cv.imshow('flower',fimg)
print(fimg.shape)
cv.waitKey(0)






# reading videos
# capture=cv.VideoCapture('CV/Videos/Video1.mp4')

# # will read video frame by frame
# # we need to resize it

# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('Video',frame)
#      # when we press letter d...video will stop
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
    
    
# capture.release()
# cv.destroyAllWindows()  




