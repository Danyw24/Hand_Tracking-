import time
import os
from serial import Serial


class droneController:
    def __init__ (self, port, baud):
        try:
            self.arduino = Serial(port, baud)
            print("[+]Puerto abierto exitosamente:")
           
        except :
            print("Error Port: El puerto no está abierto, verifique la conexion via USB ")
            os.abort()
            
                   
    def sendKey(self, key): 
        self.arduino.write(key)
        
        
        
