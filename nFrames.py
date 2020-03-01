import numpy as np
import cv2

#-----------------------------------------------------------

def initVideoCams(camNo):
    # Create Objects of VideoCapture for each Cam
    cap = []
    count = 0
    for cam in camNo:
        cap.append(cv2.VideoCapture(cam))
        print("Check Cam",cam,"Open: "+str(cap[count].isOpened()))
        # cap[count].set(3, 352)
        # cap[count].set(4, 240)
        count += 1

    return cap

def scanVideoCams(caps):
    rets = []
    frames = []
    grays = []

    # Capture frame-by-frame
    count = 0
    for cap in caps:
        rets.append(None)
        frames.append(None)
        rets[count], frames[count] = cap.read()
        count += 1

    # Our operations on the frame come here
    # count = 0
    # for frame in frames:
    #     grays.append(None)
    #     grays[count] = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     count += 1

    # Display the resulting frame
    count = 0
    for frame in frames:
        s = 'frame' + str(count)
        print(s)
        cv2.imshow(s,frame)
        count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        count = 0
        for cap in caps:
            cap.release()
            print("Check Cam ",count," Open: "+str(cap.isOpened()))
        cv2.destroyAllWindows()

def capture(caps):
    rets = []
    frames = []

    # Capture frame-by-frame
    count = 0
    for cap in caps:
        rets.append(None)
        frames.append(None)
        rets[count], frames[count] = cap.read()
        cv2.imwrite("img " + str(count) + ".png", frames[count])
        count += 1
        cap.release()
#-----------------------------------------------------------

cap = initVideoCams([0,1])
while(True):
    scanVideoCams(cap)

#-----------------------------------------------------------


