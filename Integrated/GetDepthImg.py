from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

resultDirectory = 'results'
storeResult = True

def destroyWindow():

    # plt.close('all')
    pass

def calibrationFactor():

    calibration = StereoCalibration(input_folder='calib_result')

def stereo_depth_map(rectified_pair):
    dmLeft = rectified_pair[0]
    dmRight = rectified_pair[1]
    disparity = sbm.compute(dmLeft, dmRight)
    local_max = disparity.max()
    local_min = disparity.min()
    disparity_grayscale = (disparity-local_min)*(65535.0/(local_max-local_min))
    #disparity_fixtype = cv2.convertScaleAbs(disparity_grayscale, alpha=(255.0/65535.0))
    #disparity_color = cv2.applyColorMap(disparity_fixtype, cv2.COLORMAP_JET)
    cv2.imshow("Image", disparity_grayscale)
    key = cv2.waitKey(1) & 0xFF   
    if key == ord("q"):
        quit()
    return disparity_grayscale

def getdepthImg(frameLeft, frameRight, test_num):

    # Convert Both Left & Right Images to GrayScale
    # imgL = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    # imgR = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)


    rectified_pair = calibration.rectify((frameLeft, frameRight))
    disparity = stereo_depth_map(rectified_pair)

    # stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    # disparity = stereo.compute(imgL,imgR)

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