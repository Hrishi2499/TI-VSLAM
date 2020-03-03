import numpy as np
import cv2

image = cv2.imread("test_4.jpg",0) #note: image needs to be in the opencv format
cv2.imshow("org", image)
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
# rotate the image by 180 degrees
croppedImage = image[0:h, 0:int(w/2)] #this line crops
cv2.imshow("cropped", croppedImage)
