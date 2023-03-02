#        ____                            ___  __ __
#       / __ \____ _____  __  ___      _|__ \/ // /
#      / / / / __ `/ __ \/ / / / | /| / /_/ / // /_
#     / /_/ / /_/ / / / / /_/ /| |/ |/ / __/__  __/
#    /_____/\__,_/_/ /_/\__, / |__/|__/____/ /_/   
#                      /____/                      
#   HandTracking
#   Author:Danyw24
#   Github: https://github.com/Danyw24
#   Description: Hand Tracking controller 
#   Version: Python 3.9.11
#   OS: Windows 11 MiniOS pro



import serialController
import terminalGUI
import HandsTrack
import time
import cv2
from math import hypot


#   ========================================       VALUES           ==================================================

PORT = "COM3"
BAUD = 9600
CAM = 1
WINDOW_NAME = "Hand Tracking by danyw24"
WIDTH=640
HEIGHT=480

#   ========================================       HAND TOUCH          ==================================================


def handTouch(img, lmslist, finger1,finger2, value, color, text):
    x1,y1 = lmslist[finger1][1], lmslist[finger1][2] #y
    x2,y2 = lmslist[finger2][1], lmslist[finger2][2]
    
    length = hypot(x2-x1,y2-y1)

    if int(length) <= value:
        cv2.circle(img, (x1,y1), 15, color, -1)
        cv2.putText(img, f">:{text}", (20,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        return True




#   ========================================       MAIN FUNCTION         =================================================




def main():
    drone = serialController.droneController(PORT, BAUD)
    try:
        cap = cv2.VideoCapture(CAM)
    except:
        cap = cv2.VideoCapture(0) 
        #If the cam doesnt work this will use the webcam
    #======================== CAM SETTINGS =====================
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    
    
    #===========================================================
    
    
    Handtracker = HandsTrack.HandTracking()
    pTime=0
    while True:
        success, img = cap.read()
        img  = cv2.flip(img,3)
        img = Handtracker.findHands(img)
        lmslist , handTypes= Handtracker.findPositionHands(img)
       
        
        # fps 
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime=cTime
        if (fps > 60):
            fps="60"
        cv2.putText(img, f"FPS:{int(fps)}", (20,80), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        
        
        if lmslist != []:
            for handType in handTypes:
                if handType=='Right':
                    print("RIGHT--")
                if handType=='Left':
                    print("LEFT--")
        
            # Finger detector, if true returns true boolean
            if handTouch(img,lmslist, 4,8, 34, (25,25,247), "1"):
                drone.sendKey(b'1')
            elif handTouch(img,lmslist, 4,12, 34, (25,247,102), "2"):
                drone.sendKey(b'2')
            elif handTouch(img,lmslist, 4,16, 34, (247,68,25), "3"):
                drone.sendKey(b'3')
            elif handTouch(img,lmslist, 4,20, 34, (182,25,247), "4"):
                drone.sendKey(b'4')

        cv2.imshow(WINDOW_NAME, img)
        cv2.moveWindow(WINDOW_NAME, 0,0)
        cv2.waitKey(1) # refresh time 1ms
    cap.release()           
    cv2.destroyAllWindows()


#   ========================================       ENTRY POINT          ==================================================
if __name__ == "__main__":
    main()