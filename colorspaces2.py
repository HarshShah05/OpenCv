import cv2 as cv


img=cv.imread("Pics/Indiagate.jpg")

def resizeimg(img):
    width=int(img.shape[1]/2)
    height=int(img.shape[1]/2)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("ogImg",reimg)

# Grayscale to hsv---first convert grayscale to bgr then bgr to hsv
graygate=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
cv.imshow("Graygate",graygate)

# HSV TO BGR
# we can try different combinations

hsvimg=cv.cvtColor(reimg,cv.COLOR_BGR2HSV)
cv.imshow("Hsvimage",hsvimg)

bgrimg1=cv.cvtColor(hsvimg,cv.COLOR_HSV2BGR)
cv.imshow("Bgrfromhsv",bgrimg1)
cv.waitKey(0)