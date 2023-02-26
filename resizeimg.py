import cv2 as cv

fimg=cv.imread("Pics/Mountain.jpg")
# cv.imshow("abc",fimg)
print("before resized")
print(fimg.shape)


def reimage(fimg):
    width=int(fimg.shape[1]/2)
    height=int(fimg.shape[0]/2)
    dimensions=(width,height)
    return cv.resize(fimg,dimensions)

img2=reimage(fimg)

print("After resized")
print(img2.shape)
cv.imshow("originalimg",fimg)
cv.imshow("image",img2)
cv.waitKey(0)

