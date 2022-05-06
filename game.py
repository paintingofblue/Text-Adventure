import os
import ctypes
import threading
import sys
from adventurelib import *
from items import * # type: ignore


os.system('mode con: cols=100 lines=40')

# defining colors 
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

global itemfound
global current_room # current_room will be a global variable. Let's start out in forest, so assign the 'forest' room from above.
global readpaper

readpaper = False
menu = style.RED + """\n
                     ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▄▄▄▄   ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀█▄▄▄▄ 
                    ▐  ▄▀   ▐ █ █   ▐ █ █    ▌ ▐ ▄▀ ▀▄ █   █   █ ▐  ▄▀   ▐ 
                      █▄▄▄▄▄     ▀▄   ▐ █        █▄▄▄█ ▐  █▀▀▀▀    █▄▄▄▄▄  
                      █    ▌  ▀▄   █    █       ▄▀   █    █        █    ▌  
                     ▄▀▄▄▄▄    █▀▀▀    ▄▀▄▄▄▄▀ █   ▄▀   ▄▀        ▄▀▄▄▄▄   
                     █    ▐    ▐      █     ▐  ▐   ▐   █          █    ▐   
                     ▐                ▐                ▐          ▐             
     """
inventory = []
current_room = forest # type: ignore
itemfound= False

print(menu)
print(style.WHITE + "")
print("""You've been assigned to survey the surrounding area approximately 150km from headquarters.
This comes after multiple reports of unknown disturbances from the area were shown to you.
A local farmer described his experience as "hearing an incredibly loud vibrating noise.\nHe told me it shook everything in his home. He was scared, both for his wife and dog.

In the forest, you come to a clearing, which reveals a huge temple structure. 
You decide to take a look, as this structure is something unreal.
You've never seen anything like it before in your life.\n""")


ctypes.windll.kernel32.SetConsoleTitleW("ESCAPE: A Text Adventure Game")

def getKey(obj):
    return obj.name

def check_keys():
    player_keys=[]
    for x in inventory:
        if x in keys: # If inventory item is a key, adds to player_keys
            player_keys.append(x)
    return player_keys # Return all the players keys that they currently have

@when("go DIRECTION")
def travel(direction):
    global current_room
    if direction in current_room.exits():
        current_room = current_room.exit(direction)
        print(f"You move in the direction {direction}.")
        print("You open the door to" , end = ' ') 
        print((current_room), end = ' ')
        print("")
    else: 
        print("There's nothing there. Try go in a different direction.")

@when('look')
def look():
    romexit = current_room.exits()
    romitems = current_room.items
    sortedByName2 = sorted(check_keys(), key= getKey)
    l2=[]

    if not current_room == forest and not current_room == starting_place1: # type: ignore
        print("You're currently in " , end = '') 
        print((current_room), end = '')
        print((".\n"), end = ' ')
    else:
        print("You're currently in the " , end = '') 
        print((current_room), end = '')
        print((".\n"), end = ' ')

    if not current_room == forest and not current_room == room4: # type: ignore
        print('\nThe current exits for your room are:', *romexit, sep='\n- ')
    elif current_room == forest: # type: ignore
        print('\nThe current exits for your room are:\n - east\n')
    elif current_room == room4: # type: ignore
        if keys==sortedByName2: # type: ignore
            print("""\nThere's what looks like to be an exit to the west, but it's locked.\nI'm fairly sure I have enough keys now though, as the exit has 8 key holes.""")
        else:
            print("""\nThere's what looks to be the exit to the west, but it seems to have a lock on it.\nI don't think I have enough keys to unlock it.""")

    if not current_room == forest and current_room.items != l2: # type: ignore
        print('\nThe current items you can see in the room are:', *romitems, sep='\n- ')
    elif current_room == forest: # type: ignore
        print("""There seems to be a large temple looking structure to your east. \nYou can enter the temple by typing "enter temple" below.""")
    else:
        print("\nThere are no items in this room. Try have a look around.")

def death():
    os.system('python C:\\Users\\User\\Documents\\GitHub\\Python2022\\AdventureLib\\TextAdventure\\game\\gameover.py')

# looking at item
@when('look at ITEM')
def itemlook(item):
    global readpaper
    item=conversion_dict.get(item) # type: ignore # Conversion from string input to callable object
    if item is not None:
        if item in inventory:
            if not item == paper:
                print(f"You look at the {item} in your inventory.")
                print(item.description)
            else:
                if readpaper == False:
                    print(paper.description)
                    print(style.RESET)
                    print(style.WHITE + "Hmm, The person who wrote this signed it off as \"J.\"\nI gotta get out of here! This place doesn't seem good at all, and I don't want to die.")
                    readpaper == True
                    start_time = threading.Timer(120,death)
                    start_time.start()
                else:
                    print(paper.description)
                    print(style.RESET)
                    print(style.WHITE + "I've already seen this before. I wonder how much time I have left, I certainly hope I have enough.")
        else:
            print("This item isn't in your inventory.")
    else:
        print("This item isn't in your inventory.")
    
# enter temple command
@when("enter temple")
def enter_temple():
    global current_room
    if current_room is not forest:   # type: ignore  #check if action can be done
        say("There isn't a temple here.")
        return
    else:
        current_room = starting_place1 # type: ignore
        print("""You venture into the temple, as the floor suddenly drops out beneath you.\n\nYou fall into a pit, starting to realize you are surrounded by doors.\nYou're currently at what looks like to be the starting place.\n"What the hell happened?" you yell loudly, the sound reverberating around you.\nYou see a small piece of paper laying infront of you.""")

@when("clear")
def clear():
    print("Are you sure you want to clear the game's history?\n(1) Yes\n(2) No")
    choice=int(input("Choice: "))
    if choice==1:
        print(style.RESET)
        os.system('cls')
        print(menu)
        print(style.RESET) 
    elif choice==2:
        print(style.RESET) 

# picking up items
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
    global itemfound
    for i in current_room.items: #check if item is in room
        if i.name.lower()==item.lower():
            itemfound=True

            for j in current_room.items:
                if j.name.lower()==str(item).lower():
                    item=j

            current_room.items.remove(item) #take it out of room
            inventory.append(item) #put into inventory
            print(f"You pick up the {item}.")
        else:
            continue
    if not itemfound:
        print(f"You don't see the item {item}.") #otherwise tell user there is no item
        
# inventory
l2 = []
@when("inventory")
def player_inventory():
    if inventory != l2:
        print("You are carrying")
        sortedByName = sorted(inventory, key= getKey)
        print('', *sortedByName, sep='\n- ')
    else:
        print("There is nothing in your inventory.")

@when("enter exit")
def enter_exit():
    sortedByName2 = sorted(check_keys(), key= getKey)
    global current_room
    if current_room == room4:
        if keys==sortedByName2: # If the full list of keys is equal to the players keys (if player has all keys)
            current_room = exit
            print(current_room)
            os._exit(0) 
        else:
            print("You don't have enough keys to enter the exit. Try have a look around.")
    else:
        print("There's no exit here.")

def main():
    start()

if __name__ == '__main__':
    main()