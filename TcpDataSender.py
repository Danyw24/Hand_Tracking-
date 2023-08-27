#        ____                            ___  __ __
#       / __ \____ _____  __  ___      _|__ \/ // /
#      / / / / __ `/ __ \/ / / / | /| / /_/ / // /_
#     / /_/ / /_/ / / / / /_/ /| |/ |/ / __/__  __/
#    /_____/\__,_/_/ /_/\__, / |__/|__/____/ /_/   
#                      /____/                      
#   sendData
#   Author:Danyw24
#   Github: https://github.com/Danyw24
#   Description: data sender
#   Version: Python 3.9.11
#   OS: Fedora 37


#D
import socket
import colorama
import threading
from colorama import Fore, Back, Style

#ADDRESS = "192.168.10.14"
#PORT = 8080

class DataSender:
    def __init__(self, ADDRESS, PORT):
        colorama.init()
        self.command_sent = False
        self.COMMAND_TIMEOUT = 0.5
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ADDRESS = ADDRESS
        self.PORT = PORT
      
    def ReciveConnections(self):
        self.server.bind((self.ADDRESS,self.PORT)) #Nota: se le pasa una tupla en los dos datos
        print(Fore.GREEN+ Style.BRIGHT+"[+] Servidor iniciado en {}:{}".format(self.ADDRESS,self.PORT)+ Fore.RESET)
        self.server.listen(1)
    
    
    def AcceptClient(self):
        print(Fore.CYAN +"[+] Esperando conexiones"+ Fore.RESET)
        self.client, self.client_address = self.server.accept()
        print(Fore.GREEN+ "[+] Cliente conectado {}:{}".format(self.client_address,self.PORT)+ Fore.RESET)
           
    
    def SendData(self, data):
            if not self.command_sent: 
                self.client.sendall(data.encode()) # o tambien se podria usar b
                self.command_sent = True
                threading.Timer(self.COMMAND_TIMEOUT, self.resetCommandSent).start()
            else:
                pass

            

    def ReciveData(self):
        data_recived = self.client.recv(1024) #Tamaño de el buffer a 1024 1kilobyte
        print(Fore.GREEN + "[+] Datos recibidos: \n >{}".format(data_recived.decode())+ Fore.RESET)
        return data_recived

    def CloseConnection(self):
        self.client.close()
        print(Fore.YELLOW+ "[!] Conexión cerrada"+ Fore.RESET)

    def resetCommandSent(self):
        self.command_sent = False
    
  

