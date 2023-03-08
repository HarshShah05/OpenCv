import cv2 as cv
import numpy as np
# splitmerge color channels means we gonna split the image in  3channels ie r,g,b

img=cv.imread("Pics/flower2.jpg")

def resizeimg(img):
    width=int(img.shape[1]/4)
    height=int(img.shape[0]/4)
    dimensions=(width,height)
    
    return cv.resize(img,dimensions)


reimg=resizeimg(img)
cv.imshow("Flower",reimg)

b,g,r=cv.split(reimg)
# cv.imshow("Blue",b)
# cv.imshow("Green",g)
# cv.imshow("Red",r)

# Where actually blue...for eg sky... color is there ,,,,wahape the concentration of pixels would be less that is light in color
# Where actually blue color isnt there ,,,,wahape the concentration of pixels would be more that is dark in color


# Where actually green...for eg stem of sunflower... color is there ,,,,wahape the concentration of pixels would be less that is light in color
# Where actually green color isnt there ,,,,wahape the concentration of pixels would be more that is dark in color

# merging of images

merged=cv.merge([b,g,r])
# we get back the original image
cv.imshow("Mergedimg",merged)






# Create a blank image

blank=np.ones(reimg.shape[:2],dtype='uint8')
# cv.imshow("Blank",blank)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow("Red",red)
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.waitKey(0)