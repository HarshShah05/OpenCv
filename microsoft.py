import cv2
import numpy as np

width = 1000
height = 1000


blank_image = np.ones((height, width, 3), np.uint8) * 255


top_left_color = (255, 0, 0)    
top_right_color = (0, 255, 0)   
bottom_left_color = (0, 0, 255) 
bottom_right_color = (255, 255, 0) 

cv2.rectangle(blank_image, (0, 0), (width//2, height//2), top_left_color, -1) # top left
cv2.rectangle(blank_image, (width//2, 0), (width, height//2), top_right_color, -1) # top right
cv2.rectangle(blank_image, (0, height//2), (width//2, height), bottom_left_color, -1) # bottom left
cv2.rectangle(blank_image, (width//2, height//2), (width, height), bottom_right_color, -1) # bottom right

cv2.imshow("Microsoft",blank_image)
cv2.waitKey(0)