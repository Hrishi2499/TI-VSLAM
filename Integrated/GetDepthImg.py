import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

resultDirectory = 'results'
storeResult = True

def destroyWindow():
    # plt.close('all')
    pass

def getdepthImg(frameLeft, frameRight, test_num):

    # Convert Both Left & Right Images to GrayScale [CHECK]
    imgL = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL,imgR)

    # Post Processing
    plt.imshow(disparity,'gray')
    # disparity2 = cv2.cvtColor(disparity, cv2.COLOR_BGR2GRAY)

    # Store Result in 'resultDirectory' folder
    if storeResult:
        if not os.path.exists(resultDirectory):
            os.makedirs(resultDirectory)
        cv2.imwrite(resultDirectory + '/test_'+str(test_num)+'_result.png',disparity)
    else:
        # Show Window of the Depth Image 
        plt.ion()
        plt.show()
        cv2.imshow("Depth Image", disparity)