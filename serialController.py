import time
import os
from serial import Serial

class droneController:
    def __init__ (self, PORT, BAUD):
        try:
            self.arduino = Serial(PORT, BAUD);

        except :
            print("Error Port: Error en la conexión ")
            os.abort()
            
    def sendKey(self, key): 
        key = key.encode("utf-8")
        self.arduino.write(key)
            
    

