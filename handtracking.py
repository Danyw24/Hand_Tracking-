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
#   



import serialc
import terminal_GUI
import mediapip
import time
import cv2
from math import hypot


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
    drone = serialc.droneController("COM4", 9600)
    cap = cv2.VideoCapture(1)
    Handtracker = mediapip.HandTracking()
    pTime=0
    while True:
        success, img = cap.read()
        img = Handtracker.findHands(img)
        lmslist = Handtracker.findPositionHands(img)
        # fps 
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime=cTime
        if (fps > 60):
            fps="60"
        cv2.putText(img, f"FPS:{int(fps)}", (20,80), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)


        if lmslist != []:
            # Finger detector, if true returns true boolean
            if handTouch(img,lmslist, 4,8, 30, (25,25,247), "1"):
                drone.sendKey(b'1')
            elif handTouch(img,lmslist, 4,12, 30, (25,247,102), "2"):
                drone.sendKey(b'2')
            elif handTouch(img,lmslist, 4,16, 30, (247,68,25), "3"):
                drone.sendKey(b'3')
            elif handTouch(img,lmslist, 4,20, 30, (182,25,247), "4"):
                drone.sendKey(b'4')

        cv2.imshow("name", img)
        cv2.waitKey(1) # refresh time 1ms
    cap.release()           
    cv2.destroyAllWindows()


#   ========================================       ENTRY POINT          ==================================================
if __name__ == "__main__":
    main()