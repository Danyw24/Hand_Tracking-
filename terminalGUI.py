import os
import argparse

logo_GUI = """



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
    
"""

parser = argparse.ArgumentParser(
    prog="Drone X",
    description="Drone controller with open cv2 using mediapipe for detect hands"
)

parser.add_argument("-w", "--whioutlogo", action="store_true")
args = parser.parse_args()

os.system("cls") 
if not args.whioutlogo : 
    print(logo_GUI)
   
input = input("[Drone_X]> ")
if input == "1":
    pass
elif input == "2":
    os.abort()


