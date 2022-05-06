import os
import msvcrt
import ctypes

# code to change title and resize cmd window
ctypes.windll.kernel32.SetConsoleTitleW("ESCAPE: A Text Adventure Game")
os.system('mode con: cols=100 lines=40')

# defining colors for menu text
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


while True:
    print(style.RESET)
    print(style.RED + """
                     ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄ 
                    ▐  ▄▀   ▐ █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █   █   █ ▐  ▄▀   ▐ 
                      █▄▄▄▄▄     ▀▄   ▐ █        █▄▄▄█ ▐  █▀▀▀▀    █▄▄▄▄▄  
                      █    ▌  ▀▄   █    █       ▄▀   █    █        █    ▌  
                     ▄▀▄▄▄▄    █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀   ▄▀        ▄▀▄▄▄▄   
                     █    ▐    ▐      █     ▐  ▐   ▐   █          █    ▐   
                     ▐                ▐                ▐          ▐             
     """) # centered ascii for menu
    print(style.WHITE + "")
    print("Choose an option:\n(1) Play Game\n(2) Quit")
    try:
        choice=int(input("Choice: "))
        if choice==1:
            print(style.RESET)
            os.system('python C:\\Users\\User\\Documents\\GitHub\\Python2022\\AdventureLib\\TextAdventure\\game\\game.py')
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