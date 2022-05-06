import os
import time
import msvcrt

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

menu = style.RED + """\n
                     ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄ 
                    ▐  ▄▀   ▐ █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █   █   █ ▐  ▄▀   ▐ 
                      █▄▄▄▄▄     ▀▄   ▐ █        █▄▄▄█ ▐  █▀▀▀▀    █▄▄▄▄▄  
                      █    ▌  ▀▄   █    █       ▄▀   █    █        █    ▌  
                     ▄▀▄▄▄▄    █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀   ▄▀        ▄▀▄▄▄▄   
                     █    ▐    ▐      █     ▐  ▐   ▐   █          █    ▐   
                     ▐                ▐                ▐          ▐             
     """

os.system('cls')

while True:
    print(style.RESET)
    print(menu)
    print(style.RESET)
    print("\n\n\"Wait, what's that sound?\" I say as I feel a wave of fatigue fall over me.\nA deep, distorted voice bellows out over the loudspeaker, saying the following:\n\n\"Unfortunately, you didn't escape in time. We will be taking your belongings,\nand due to the ammonia, you will die.\nYou will not have a chance to say your goodbyes.\n\nFarewell, old friend.\"")
    print("\n\nWould you like to play again?")
    print("Choose an option:\n(1) Yes\n(2) No")
    try:
        choice=int(input("Choice: "))
        if choice==1:
            print(style.RESET)
            os.system('python C:\\Users\\User\\Documents\\GitHub\\Python2022\\AdventureLib\\TextAdventure\\menu.py')
        elif choice==2:
            print(style.RESET)
            os.system("cls")
            os._exit(0) 
        else:
            print(style.UNDERLINE + "That was an incorrect answer. Press any key to continue")
            print(style.RESET)
            msvcrt.getch()
        os.system("cls")
    except:
        print(style.UNDERLINE + "That was an incorrect answer. Press any key to continue")
        print(style.RESET)
        msvcrt.getch()
        os.system('cls')
        continue
