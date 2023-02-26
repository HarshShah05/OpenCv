import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Compute histograms for rgb images and greyscale images
img=cv.imread("Pics/sungirl.jpg")
def resizeimg(img):
    width=int(img.shape[1]/10)
    height=int(img.shape[1]/10)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("Girl",reimg)
graygirl=cv.cvtColor(reimg,cv.COLOR_BGR2GRAY)
rgbgirl=cv.cvtColor(reimg,cv.COLOR_BGR2RGB)
# cv.imshow("Graygirl",graygirl)
# cv.imshow("RGB",rgbgirl)

# histisze is basically bins
# bins represent intensity of pixel
# gray_hist=cv.calcHist([graygirl],[0],None,[256],[0,256])
# plt.figure()
# plt.title("Grayscale histogram" )
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.show()

colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist(reimg,[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.figure()
# plt.title("color histogram" )
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
plt.show()

cv.waitKey(0)


