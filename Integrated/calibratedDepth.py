import time
import cv2
import numpy as np
import json
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from datetime import datetime
from matplotlib import pyplot as plt

# Depth map default preset
SWS = 5
PFS = 5
PFC = 29
MDS = -30
NOD = 160
TTH = 100
UR = 10
SR = 14
SPWS = 100
img_width, img_height = 640, 480
calibResultFolder = 'calibration/calib_result'
calibration = None
disparity = None
sbm = None

def CreateCalibObject(calibResultFolder):
    # Implementing calibration data
    global calibration
    print('Read calibration data and rectifying stereo pair...')
    calibration = StereoCalibration(input_folder=calibResultFolder)

def InitDisparityAndSBM(img_width, img_height):
    global disparity
    global sbm
    disparity = np.zeros((img_width, img_height), np.uint8)
    sbm = cv2.StereoBM_create(numDisparities=0, blockSize=21)

def StereoDepthImage(rectified_pair, ConvertionType):
    if(ConvertionType=="sbm"):
        dmLeft = cv2.cvtColor(rectified_pair[0], cv2.COLOR_BGR2GRAY)
        dmRight = cv2.cvtColor(rectified_pair[1], cv2.COLOR_BGR2GRAY)
        disparity = sbm.compute(dmLeft, dmRight)
        local_max = disparity.max()
        local_min = disparity.min()
        disparity_grayscale = (disparity-local_min)*(65535.0/(local_max-local_min))
        disparity_fixtype = cv2.convertScaleAbs(disparity_grayscale, alpha=(255.0/65535.0))
        disparity_color = cv2.applyColorMap(disparity_fixtype, cv2.COLORMAP_JET)
        key = cv2.waitKey(1) & 0xFF   
        if key == ord("q"):
            quit()
        return disparity_color
        
    elif(ConvertionType=="cv2"):
        # Convert Both Left & Right Images to GrayScale [CHECK]
        imgL = cv2.cvtColor(rectified_pair[0], cv2.COLOR_BGR2GRAY)
        imgR = cv2.cvtColor(rectified_pair[1], cv2.COLOR_BGR2GRAY)

        stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
        disparity = stereo.compute(imgL,imgR)

        # Post Processing
        # plt.imshow(disparity,'gray')
        # disparity2 = cv2.cvtColor(disparity, cv2.COLOR_BGR2GRAY)

        return disparity
        #cv2.imwrite(resultDirectory + '/test_'+str(test_num)+'_result.png',disparity)

def InitInterface():
    # Initialize interface windows
    cv2.namedWindow("Image")
    cv2.moveWindow("Image", 50,100)
    cv2.namedWindow("left")
    cv2.moveWindow("left", 450,100)
    cv2.namedWindow("right")
    cv2.moveWindow("right", 850,100)

# Main Executions
CreateCalibObject(calibResultFolder)
InitDisparityAndSBM(img_width, img_height)

# capture frames from the camera
cap1 = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(1)

while(True):
    # Capturing Left and Right Images
    ret1, imgLeft = cap1.read()
    ret2, imgRight = cap2.read()
    cv2.imshow("left", imgLeft)
    cv2.imshow("right", imgRight)   

    # Pre-Processing using Rectifier
    rectified_pair = calibration.rectify((imgLeft, imgRight))

    # Depth Conversion
    disparity = StereoDepthImage(rectified_pair, "sbm")
    #disparity2 = StereoDepthImage(rectified_pair, "cv2")

    cv2.imshow("SBM", disparity)
    #cv2.imshow("CV2", disparity2)

    # Wait Key to Destroy Windows 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
