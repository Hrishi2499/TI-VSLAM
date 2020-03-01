import numpy as np
import cv2

#-----------------------------------------------------------

def initVideoCams(camNo1, camNo2):
    # Create Objects of VideoCapture for each Cam
    cap = [None,None]
    cap[0] = cv2.VideoCapture(camNo1)
    cap[1] = cv2.VideoCapture(camNo2)
    print("Check Cam 2 Open: "+str(cap[0].isOpened()))
    print("Check Cam 4 Open: "+str(cap[1].isOpened()))
    return cap

def scanVideoCams(cap1, cap2):
    # Capture frame-by-frame
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # Our operations on the frame come here
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame1',frame1)
    cv2.imshow('frame2',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        closeVideoCams(cap1, cap2)

def closeVideoCams(cap1, cap2):
    # When everything done, release the capture
    cap1.release()
    cap2.release()
    print("Check Cam 2 Open: "+str(cap[0].isOpened()))
    print("Check Cam 4 Open: "+str(cap[1].isOpened()))
    cv2.destroyAllWindows()

#-----------------------------------------------------------

cap = initVideoCams(0,2)
while(True):
    scanVideoCams(cap[0],cap[1])

#-----------------------------------------------------------


