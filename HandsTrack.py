import mediapipe as mp
import cv2


class HandTracking:
    def __init__(self, mode = False, maxHands = 2, minDetectionConfidence = 0.5, minTrackingConfidence= 0.5):
        
        self.mode = mode
        self.maxHands = maxHands
        self.minDetectionConfidence = minDetectionConfidence
        self.minTrackingConfidence =  minTrackingConfidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode , self.maxHands, self.minDetectionConfidence,  self.minTrackingConfidence)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
            


    def findPositionHands(self, img ,handNo = 0, draw = False, radius = 10, color = [0,255,0], thickness = cv2.FILLED):
        lmslist = []
        handsType = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_handedness:
                
                hand = self.results.multi_hand_landmarks[handNo]
              
                for id, lm in enumerate(hand.landmark):
                    h, w, c = img.shape
                    cx , cy = int( lm.x * w), int ( lm.y * h)
                    lmslist.append([id,cx,cy])
                
                for hand in self.results.multi_handedness:
                    handType = hand.classification[0].label
                    handsType.append(handType)
                    
                    
                if draw:
                    cv2.circle(img, (cx,cy), radius, color, thickness)
        return lmslist, handsType





        
        




