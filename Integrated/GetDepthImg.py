import numpy as np
import cv2
from matplotlib import pyplot as plt

resultDirectory = 'results'
storeResult = True

def destroyWindow():
    # plt.close('all')
    pass

def getdepthImg(imgL, imgR, test_num):
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL,imgR)
    plt.imshow(disparity,'gray')
    # disparity2 = cv2.cvtColor(disparity, cv2.COLOR_BGR2GRAY)
    if storeResult:
        cv2.imwrite(resultDirectory + '/test_'+str(test_num)+'_result.png',disparity)
    # plt.show()
    cv2.imshow("Depth Image", disparity)