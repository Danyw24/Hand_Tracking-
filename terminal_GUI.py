import os

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
"""




print(logo_GUI)
if input(" >"):
    pass


def gui_finger(text):
    os.system("cls")
    print(f"""


:::::::-.  :::::::..       ...   :::.    :::..,::::::    .,::      .:
 ;;,   `';,;;;;``;;;;   .;;;;;;;.`;;;;,  `;;;;;;;''''    `;;;,  .,;; 
 `[[     [[ [[[,/[[['  ,[[     \[[,[[[[[. '[[ [[cccc       '[[,,[['  
  $$,    $$ $$$$$$c    $$$,     $$$$$$ "Y$c$$ $$""''        Y$$$P    
  888_,o8P' 888b "88bo,"888,_ _,88P888    Y88 888oo,__    oP"``"Yo,  
  MMMMP"`   MMMM   "W"   "YMMMMMP" MMM     YM ""''YUMMM,m'       'Mm,


        [+] {text}


""")
    

