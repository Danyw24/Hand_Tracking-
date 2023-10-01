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
#   OS: Fedora 37



import serialController
import terminalGUI
from terminalGUI import whioutArduino
import HandsTrack
import os
import colorama
from colorama import Fore, Back, Style
import time
import cv2
from math import hypot


#   ========================================       VALUES           ==================================================
colorama.init()
PORT = "/dev/ttyUSB0"
BAUD = 9600
CAM = 0
WINDOW_NAME = "Hand Tracking by danyw24"
WIDTH=640
HEIGHT=480
#ADDRESS = "172.20.10.36"
#NET_PORT= 8080

#   ========================================       HAND TOUCH          ==================================================


def handTouch(img, lmslist, finger1,finger2, value, color, text):
    x1,y1 = lmslist[finger1][1], lmslist[finger1][2] #y
    x2,y2 = lmslist[finger2][1], lmslist[finger2][2]
    
    length = hypot(x2-x1,y2-y1)

    if int(length) <= value:
        cv2.circle(img, (x1,y1), 15, color, -1)
        cv2.putText(img, f">:{text}", (20,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        return True


def detectDepthOfFand(img, lmslist, finger1,finger2, depht, depht2, color, text):
    x1,y1 = lmslist[finger1][1], lmslist[finger1][2] #y
    x2,y2 = lmslist[finger2][1], lmslist[finger2][2]
    
    length = hypot(x2-x1,y2-y1)

    if int(length) <= depht  and int(length >= depht2):
        cv2.line(img,(x1,y1),(x2,y2), color, 2)
        cv2.putText(img, f">:{length.__ceil__()}", (20,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
        return True



#   ========================================       MAIN FUNCTION         =================================================




def main():
    if not whioutArduino:
        drone = serialController.droneController(PORT, BAUD)
    else:
        drone = None

    def sendKey(key):
        if drone:
            drone.sendKey(key)
     
    
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
            #for handType in handTypes:
             #   if handType=='Right':
              #      print("RIGHT--")
               # if handType=='Left':
                #    print("LEFT--")
        
            # Finger detector, if true returns true boolean

            #STEP BACK

            #if detectDepthOfFand(img,lmslist, 0,9, 100, 80, (153, 255, 51), "1"):
              #  sendKey("3\n")

            #STEP UP

            #if detectDepthOfFand(img,lmslist, 0,9, 170, 140, (0, 0, 255), "1"):
             #   sendKey("2\n")


            if handTouch(img,lmslist, 4,8, 34, (255, 221, 51), "2"):
                sendKey("up\n")
            if handTouch(img,lmslist, 4,12, 34, (0, 204, 204), "2"):
                sendKey("down\n")
            if handTouch(img,lmslist, 4,16, 34, (255, 51, 153), "3"):
                sendKey("left\n")
            if handTouch(img,lmslist, 4,20, 34, (255, 153, 51), "4"):
                sendKey("right\n")

        cv2.imshow(WINDOW_NAME, img)
        cv2.moveWindow(WINDOW_NAME, 0,0)
        cv2.waitKey(1) # refresh time 1ms
    cap.release()           
    cv2.destroyAllWindows()


#   ========================================       ENTRY POINT          ==================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.YELLOW,"\n\n[+] Gracias por usar mi programa :) \n",Fore.RESET)

