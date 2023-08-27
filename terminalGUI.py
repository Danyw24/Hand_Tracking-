#ARGUMENTS
# [1]. No drone use
# [2]. Init whiout logo
# [3]. Help 


import os
import argparse
import colorama
from colorama import Fore, Back, Style
import platform


logoGUI = """



:::::::-.  :::::::..       ...   :::.    :::..,::::::    .,::      .:
 ;;,   `';,;;;;``;;;;   .;;;;;;;.`;;;;,  `;;;;;;;''''    `;;;,  .,;; 
 `[[     [[ [[[,/[[['  ,[[     \[[,[[[[[. '[[ [[cccc       '[[,,[['  
  $$,    $$ $$$$$$c    $$$,     $$$$$$ "Y$c$$ $$""''        Y$$$P    
  888_,o8P' 888b "88bo,"888,_ _,88P888    Y88 888oo,__    oP"``"Yo,  
  MMMMP"`   MMMM   "W"   "YMMMMMP" MMM     YM ""''YUMMM,m'       'Mm,

    [+] Developed by danyw24 - 2023

    [*] Select an option:

    [1]. Start program 
    
    [2]. Abort program

    [3]. Help
    
"""




helpLogoScreen = f"""
MMWMMMMMO'.kWWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWMWWk.'OWMMMMMMM
l:::::::'  ':::::::l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0l:::::::'  ':::::::l
.                  .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.                  .
0kkkkkkkc. :kkkkkkk0NMMWOollllllllllllllllllllllloOWMMN0kkkkkkk: .ckkkkkkk0
MMMMMMMO,  'kWMMMMMMMMM0'                         '0MMMMMMMMMWk'  ,OMMMMMMM
MMMMMMWo    lWMMMMMMMMMO.        .;clolc;.        .OMMMMMMMMMWl    oWMMMMMM
MMMMMMWo    'looooooooo:.      .oKWMWWWMWKo.      .:oooooooool'    oWMMMMMM
MMMMMMWo                      .kWWKo;;;oKWWk.                      oWMMMMMM
MMMMMMWo     .............    :XMNc     cNMN:    .............     oWMMMMMM
MMMMMMWo    :0KKKKKKKKKKKk;   ,0MWk,...,kWMK,   ,kKKKKKKKKKKK0:    oWMMMMMM
MMMMMMMKocco0MMMMMMMMWKdc'.    ;0WMNKKKNMW0;    .'cd0WMMMMMMMW0occoKMMMMMMM
MMMMMMMMMMMMMMMMMMWKd;.     .   .:dkO0Okd:.         .;dKWMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWKl.    .:dOx.               .lOd:.    .lKWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNd.   .;xXWMMX:               '0MMWXx;.   .dNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMXl.   ;OWMMMMMWO;.............'dNMMMMMWO;    lXMMMMMMMMMMMMMM
MMMMMMMMMMMMMXc   .oNMMMMMMMMMNXKKKKKKKKKKKKNWMMMMMMMMNo.   cXMMMMMMMMMMMMM
MMMMMMMMMMMMWd.  .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.  .dWMMMMMMMMMMMM
MMMMMMMMMMMMK;   ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX;   ;KMMMMMMMMMMMM
MMMMMMMMMMMMk.   dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd   .kMMMMMMMMMMMM
MMMMMMMMMMMMk.  .kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk.  .kMMMMMMMMMMMM
MMMMMMMMMMMMK;  :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:  ;KMMMMMMMMMMMM


    ==========================================================
            SISTEMA DE CONTROL DE DRON CON MANOS           
    ==========================================================

Bienvenido al sistema de control de dron con manos. 

Instrucciones:
1. Asegúrate de que la cámara esté configurada y funcione correctamente.
2. Coloca tus manos frente a la cámara para que sean detectadas.
3. Utiliza los siguientes comandos para controlar el dron:

   - "t": Despegar el dron.
   - "l": Aterrizar el dron.
   - "u": Mover el dron hacia arriba.
   - "d": Mover el dron hacia abajo.
   - "f": Mover el dron hacia adelante.

4. Si necesitas ayuda adicional, consulta el readme.md en github.

¡Diviértete controlando el dron con tus manos!

==========================================================
"""
colorama.init()
OS = platform.system()

if OS == "windows":
    clearCommand = "cls"
    ipCommand = None
elif OS == "Linux":
    clearCommand = "clear"

whioutArduino = False

parser = argparse.ArgumentParser(
    prog="Drone X",
    description=f"Drone controller with open cv2 using mediapipe for detect hands"
)

parser.add_argument("-w", "--whioutlogo", action="store_true")
parser.add_argument("-wA","--whiout-arduino", action="store_true")
args = parser.parse_args()

os.system(clearCommand) 




def initUI():
    while True:
        os.system(clearCommand) 
        print(logoGUI)
        response = input(Back.CYAN+"[DroneX]> "+Back.RESET)
        if response == "1":
            break
        elif response == "2":
            os.abort()
        elif response == "3":
            os.system(clearCommand)
            print(helpLogoScreen)
            os.abort()
            break



if args.whiout_arduino:
    whioutArduino = True


if not args.whioutlogo: 
    initUI()
   

   
   
