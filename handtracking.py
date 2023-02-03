#
#   ------------------------                                                         
#   ------------------------          ___                        ___ ____             
#   ------------------------         / _ \___ ____  __ ___    __|_  / / /              
#   ------------------------        / // / _ `/ _ \/ // / |/|/ / __/_  _/              
#   ------------------------       /____/\_,_/_//_/\_, /|__,__/____//_/                  
#   ------------------------                      /___/                                 
#   ------------------------       
#
#   Author: danyw24
#   Github: https://github.com/danyw24

import cv2
import mediapipe as mp
capture = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


#------------------------------------- Captura de camara y manos ---------------------------------
while True:
    #--------------------------------- Analiza el fotograma con el modulo cv2 --------------------
    success, image = capture.read()   
    # --------------------- El modulo mediapipe solo acepta imagenes en formato RGB lo cual es necesario configurar la imagen de BGR a RGB
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    #-------------------------- Si, hay existencia de puntos de manos, hacer el muestreo en el fotograma a mostrar
    if results.multi_hand_landmarks:
        for handsLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(image, handsLms, mpHands.HAND_CONNECTIONS)
    #------------------------------ Titulo de la ventana y como segundo parametro el fotograma ya modificado --------
    cv2.imshow("Test",image)
    cv2.waitKey(1)
capture.release()
cv2.destroyAllWindows()
