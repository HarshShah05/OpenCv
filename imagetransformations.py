import cv2 as  cv
import numpy as  np

# Translation
# Rotation
# Flipping

nimg=cv.imread('Pics/Nature.jpg')


def resizeimage(nimg):
    width=int(nimg.shape[1]/2)
    height=int(nimg.shape[0]/2)
    dimensions=(width,height)
    return cv.resize(nimg,dimensions)

reimg=resizeimage(nimg)
cv.imshow("nature",reimg)

# Translation

def translation(reimg,x,y):
    # create translation matrix
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(reimg.shape[1],reimg.shape[0])
    # wrap affine takes image,its matrix and dimensions
    return cv.warpAffine(reimg,transmat,dimensions)

# -x -->Left
# -y -->Up
# x -->Right
#y-->Down
# shift in x and y by 100 pixels
translatedimg=translation(reimg,-100,100)
cv.imshow("Transimg",translatedimg)

    
    



# Rotation
# rotpoint---point from where we are rotating
def rotation(reimg,angle):
    (height,width)=reimg.shape[:2]
    rotpoint=(width//2,height//2)
    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions=(height,width)
    return cv.warpAffine(reimg,rotmat,dimensions)
    
rotatedimg=rotation(reimg,45)
# -45 == rotates clockwise
cv.imshow("Rotated image",rotatedimg)



# Flipping
# 0==flip vertically
# 1==flip horizantaly

flipimage=cv.flip(reimg,0)
cv.imshow("Flipped",flipimage)
cv.waitKey(0)