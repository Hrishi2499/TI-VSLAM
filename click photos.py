import time
import numpy as np
import cv2

left = 1
right = 0
directory = "dataset/"
sleepTime = 0.1

#-----------------------------------------------------------

def initVideoCams():
    # Create Objects of VideoCapture for each Cam
    
    capLeft = cv2.VideoCapture(left)
    capRight = cv2.VideoCapture(right)
    print("Check Cam Left Open: "+str(capLeft.isOpened()))
    print("Check Cam Left Open: "+str(capRight.isOpened()))
    # cap[count].set(3, 352)
    # cap[count].set(4, 240)

    return capLeft, capRight

def scanVideoCams(capLeft, capRight):

    # Capture frame-by-frame
    retLeft, frameLeft = capLeft.read()
    retRight, frameRight = capRight.read()

    # Our operations on the frame come here
    # count = 0
    # for frame in frames:
    #     grays.append(None)
    #     grays[count] = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     count += 1

    # Display the resulting frame
    cv2.imshow('Left',frameLeft)
    cv2.imshow('Right',frameRight)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        capLeft.release()
        capRight.release()
        print("Check Cam Left Open: "+str(capLeft.isOpened()))
        print("Check Cam Right Open: "+str(capRight.isOpened()))
        cv2.destroyAllWindows()

def capture(capLeft, capRight, count):
    # Capture frame-by-frame
    retLeft, frameLeft = capLeft.read()
    retRight, frameRight = capRight.read()
    cv2.imwrite(directory+"img_left_" + str(count) + ".png", frameLeft)
    cv2.imwrite(directory+"img_right_" + str(count) + ".png", frameRight)
    print("Written",str(count))
#---------------------------------
# --------------------------

capLeft, capRight = initVideoCams()
count = 0
start_time = time.time()
once = -1
while(True):
    end_time = time.time()
    scanVideoCams(capLeft, capRight)   
    if True: #int(end_time-start_time) % sleepTime == 0 and int(end_time-start_time) != once:
        once = int(end_time-start_time)
        capture(capLeft, capRight, count)   
        count += 1
        time.sleep(0.1)

capLeft.release()
capRight.release()
#-----------------------------------------------------------


