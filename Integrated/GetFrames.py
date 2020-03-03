import time
import numpy as np
import cv2
import os
import GetDepthImg

left = 4    #Left Camera
right = 2   #Right Camera
storeDirectory = "dataset"
interval = 1
storeMode = True

def initVideoCams():
    # Create Objects of VideoCapture for each Cam
    
    capLeft = cv2.VideoCapture(left)
    capRight = cv2.VideoCapture(right)
    print("Check Cam Left Open: "+str(capLeft.isOpened()))
    print("Check Cam Left Open: "+str(capRight.isOpened()))

    return capLeft, capRight

def scanVideoCams(capLeft, capRight):

    # Capture frame-by-frame
    retLeft, frameLeft = capLeft.read()
    retRight, frameRight = capRight.read()

    # Display the resulting frame
    cv2.imshow('Left',frameLeft)
    cv2.imshow('Right',frameRight)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        capLeft.release()
        capRight.release()
        print("Check Cam Left Open: "+str(capLeft.isOpened()))
        print("Check Cam Right Open: "+str(capRight.isOpened()))
        cv2.destroyAllWindows()

def captureAndPost(capLeft, capRight, count):
    # Capture frame-by-frame
    retLeft, frameLeft = capLeft.read()
    retRight, frameRight = capRight.read()

    grayLeft = cv2.cvtColor(frameLeft, cv2.COLOR_BGR2GRAY)
    grayRight = cv2.cvtColor(frameRight, cv2.COLOR_BGR2GRAY)

    GetDepthImg.getdepthImg(grayLeft, grayRight, count)

    if (storeMode):
        if not os.path.exists(storeDirectory):
            os.makedirs(storeDirectory)
        cv2.imwrite(storeDirectory+"/test_" + str(count) + "_l.png", frameLeft)
        cv2.imwrite(storeDirectory+"/test_" + str(count) + "_r.png", frameRight)
        print("Written",str(count))

    

capLeft, capRight = initVideoCams()
count = 0
start_time = time.time()
once = -1
while(True):
    end_time = time.time()
    # scanVideoCams(capLeft, capRight)   
    if int(end_time-start_time) % interval == 0 and int(end_time-start_time) != once:
        once = int(end_time-start_time)
        captureAndPost(capLeft, capRight, count)   
        GetDepthImg.destroyWindow()
        count += 1
        # time.sleep(0.1)

capLeft.release()
capRight.release()


