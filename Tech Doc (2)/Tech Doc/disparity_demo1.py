import numpy as np
import cv2
from matplotlib import pyplot as plt

test_num =5
splitMode =True

### load the image and show it
##image = cv2.imread('dataset/test_'+str(test_num)+'.png')
##cv2.imshow("original", image)
##cv2.waitKey(0)
##
### grab the dimensions of the image and calculate the center
### of the image
##(h, w) = image.shape[:2]
##
### crop the image using array slices -- it's a NumPy array
### after all!
##cropped_left = image[0:int(h), 0:int(w/2)]
##cropped_right = image[0:int(h), int(w/2):int(w)]
##cv2.imshow("cropped left", cropped_left)
##cv2.imshow("cropped right", cropped_right)
##cv2.waitKey(0)
##
##imgL = cropped_left
##imgR = cropped_right

if(splitMode==True):
    image = cv2.imread('dataset/test_'+str(test_num)+'.jpg',0)
    (h, w) = image.shape[:2]
    imgL = image[0:h, 0:int(w/2)]
    imgR = image[0:h, int(w/2):w]
    cv2.imshow("left",imgL)
    cv2.imshow("right",imgR)
else:
    imgL = cv2.imread('dataset/test_'+str(test_num)+'_l.jpg',0)
    imgR = cv2.imread('dataset/test_'+str(test_num)+'_r.jpg',0)


stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
cv2.imwrite('results/test_'+str(test_num)+'_result.png',disparity)
plt.show()

