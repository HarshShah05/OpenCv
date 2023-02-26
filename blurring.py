import cv2 as cv
import numpy as np

# gaussian
# bilateral blur
# median blur
# average blur




img=cv.imread("Pics/teddy.jpg")
def resizeimg(img):
    width=int(img.shape[1]/10)
    height=int(img.shape[1]/10)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("Teddy",reimg)

Gaussianblur=cv.GaussianBlur(reimg,(3,3),cv.BORDER_DEFAULT)
cv.imshow("gausian blur",Gaussianblur)




# cv.blur averages out all pixels value and adds them to centre and blurs it
averageblur=cv.blur(reimg,(3,3))
cv.imshow("averageblur",averageblur)




# median blur...finds median of all running pixels
# it helps in decreasing noise
medianblur=cv.medianBlur(reimg,3)
cv.imshow("Medianblur",medianblur)



# bilateralblur
# sigmacolor--More colors in neighbourhood ,that will be considered when blur is completed
# sigmaface---larger value means pixes further out from centre pixel
bblur=cv.bilateralFilter(reimg,15,45,45)
cv.imshow("Bilateralblur",bblur)
cv.waitKey(0)