import time
import cv2
import numpy as np
import json
from stereovision.calibration import StereoCalibrator
from stereovision.calibration import StereoCalibration
from datetime import datetime

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

# Camera settimgs
cam_width = 1280
cam_height = 480

# Final image capture settings
scale_ratio = 0.5

# Camera resolution height must be dividable by 16, and width by 32
cam_width = int((cam_width+31)/32)*32
cam_height = int((cam_height+15)/16)*16
print ("Used camera resolution: "+str(cam_width)+" x "+str(cam_height))

# Buffer for captured image settings
img_width = int (cam_width * scale_ratio)
img_height = int (cam_height * scale_ratio)
capture = np.zeros((img_height, img_width, 4), dtype=np.uint8)
print ("Scaled image resolution: "+str(img_width)+" x "+str(img_height))



# Implementing calibration data
print('Read calibration data and rectifying stereo pair...')
calibration = StereoCalibration(input_folder='calib_result')

# Initialize interface windows
cv2.namedWindow("Image")
cv2.moveWindow("Image", 50,100)
cv2.namedWindow("left")
cv2.moveWindow("left", 450,100)
cv2.namedWindow("right")
cv2.moveWindow("right", 850,100)


disparity = np.zeros((img_width, img_height), np.uint8)
sbm = cv2.StereoBM_create(numDisparities=0, blockSize=21)

def stereo_depth_map(rectified_pair):
    dmLeft = cv2.cvtColor(rectified_pair[0], cv2.COLOR_BGR2GRAY)
    dmRight = cv2.cvtColor(rectified_pair[1], cv2.COLOR_BGR2GRAY)
    disparity = sbm.compute(dmLeft, dmRight)
    local_max = disparity.max()
    local_min = disparity.min()
    disparity_grayscale = (disparity-local_min)*(65535.0/(local_max-local_min))
    #disparity_fixtype = cv2.convertScaleAbs(disparity_grayscale, alpha=(255.0/65535.0))
    #disparity_color = cv2.applyColorMap(disparity_fixtype, cv2.COLORMAP_JET)
    cv2.imshow("Image", disparity_grayscale)
    key = cv2.waitKey(1) & 0xFF   
    if key == ord("q"):
        quit();
    return disparity_grayscale

# def load_map_settings( fName ):
#     global SWS, PFS, PFC, MDS, NOD, TTH, UR, SR, SPWS, loading_settings
#     print('Loading parameters from file...')
#     f=open(fName, 'r')
#     data = json.load(f)
#     SWS=data['SADWindowSize']
#     PFS=data['preFilterSize']
#     PFC=data['preFilterCap']
#     MDS=data['minDisparity']
#     NOD=data['numberOfDisparities']
#     TTH=data['textureThreshold']
#     UR=data['uniquenessRatio']
#     SR=data['speckleRange']
#     SPWS=data['speckleWindowSize']    
#     #sbm.setSADWindowSize(SWS)
#     sbm.setPreFilterType(1)
#     sbm.setPreFilterSize(PFS)
#     sbm.setPreFilterCap(PFC)
#     sbm.setMinDisparity(MDS)
#     sbm.setNumDisparities(NOD)
#     sbm.setTextureThreshold(TTH)
#     sbm.setUniquenessRatio(UR)
#     sbm.setSpeckleRange(SR)
#     sbm.setSpeckleWindowSize(SPWS)
#     f.close()
#     print ('Parameters loaded from file '+fName)


# load_map_settings ("set.txt")

# capture frames from the camera
cap1 = cv2.VideoCapture(4)
cap2 = cv2.VideoCapture(2)
while(True):
    t1 = datetime.now()
    ret1, imgLeft = cap1.read()
    ret2, imgRight = cap2.read()
     #Y+H and X+W
    rectified_pair = calibration.rectify((imgLeft, imgRight))
    disparity = stereo_depth_map(rectified_pair)
    # show the frame
    cv2.imshow("left", imgLeft)
    cv2.imshow("right", imgRight)    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    t2 = datetime.now()
    print ("DM build time: " + str(t2-t1))
