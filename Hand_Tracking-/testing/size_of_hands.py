#


import HandsTrack
import cv2
from math import hypot

cap = cv2.VideoCapture(1)
hands = HandsTrack.HandTracking()

def getSizeOfHands(lmslist, finger1, finger2):
    x1,y1 = lmslist[finger1][1], lmslist[finger1][2] #y
    x2,y2 = lmslist[finger2][1], lmslist[finger2][2]
    
    length = int(hypot(x2-x1,y2-y1))
    
    if length >= 100 and length <= 150:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0), 4)
        print("estable")
    else:
        print("No estable")

while True:
    success , img = cap.read()
    img = hands.findHands(img)
    lmslist, handsTypes = hands.findPositionHands(img)                          
    if lmslist:
        getSizeOfHands(lmslist,0,9)
    cv2.imshow("test",img)
    cv2.waitKey(1)    


