from adventurelib import *

inventory = Bag()

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

# defining rooms 
forest = Room("""Forest""")
starting_place1 = Room("""starting area""")
room1 = Room("""Room 1""")
room2 = Room("""Room 2""")
room3 = Room("""Room 3""")
room4 = Room("""Room 4""")
room5 = Room("""Room 5""")
room6 = Room("""Room 6""")
room7 = Room("""Room 7""")
room8 = Room("""Room 8""")
exit = Room("""You beat the game and escaped the temple!""")

# creating connections
starting_place1.east = room1
starting_place1.north = room3
starting_place1.south = room7
room1.north = room2
room7.east = room8
room8.east = room6
room6.north = room5
room3.west = room4

# Items
Item.description = "" #adds a blank description to each number

# definte items
paper = Item('Paper')
key1 = Item('Room 1 Key')
key2 = Item('Room 2 Key')
key3 = Item('Room 3 Key')
key4 = Item('Room 4 Key')
key5 = Item('Room 5 Key')
key6 = Item('Room 6 Key')
key7 = Item('Room 7 Key')
key8 = Item('Room 8 Key')
test = Item('test')

# defining descriptions for each item, need to switch it up for each one. can use https://quillbot.com

paper.description = "The paper reads as follows:\n\n\"Hello, if you're reading this you've fallen into my trap.\nThe team have designed this escape room to disperse a " + style.RED + style.UNDERLINE + "lethal dosage of ammonia" + style.RESET + " immediately after \nyou have finished reading this piece of paper. \nYou will have 2 minutes to escape this building, starting from now.\nGood luck.\""
key1.description = "\nThe key's exterior has been damaged severely, and a red number 1 has been carved into it.\n\nYou could try to find an exit to use it on?"
key2.description = "\nThe exterior of the key has been ravaged, with a red number 2 carved into it.\nMaybe try to find an exit to use it on?"
key3.description = "\nThe key's exterior has been ravaged, and a red number 3 has been carved into it.\nYou could try to find an exit to use it on?"
key4.description = "\nThe key's exterior is ravaged, with a red number 4 carved into it.\nMaybe try to find an exit to use it on?"
key5.description = "\nThe key has been defiled on the exterior, and a number 5 has been etched into it.\nYou could try to find an exit to use it on?"
key6.description = "\nThe key's exterior has been mangled, and the number 6 has been etched into it.\nMaybe try to find an exit to use it on?"
key7.description = "\nThe exterior of the key is ravaged, and a number 7 is carved into it.\nYou could try to find an exit to use it on?"
key8.description = "\nThe key's outside is damaged, with a number 8 cut into it. \nMaybe try to find an exit to use it on?"

# room locks defining
room2.locked = True
room4.locked = True
room5.locked = True
room6.locked = True
room8.locked = True

# defining room descriptions


# define lists
starting_place1.items = [paper]
room1.items = [key1]
room2.items = [key2]
room3.items = [key3]
room4.items = [key4]
room5.items = [key5]
room6.items = [key6]
room7.items = [key7]
room8.items = [key8]
forest.items = [test]

conversion_dict={
    'paper':paper,
    'room 1 key':key1,
    'room 2 key':key2,
    'room 3 key':key3,
    'room 4 key':key4,
    'room 5 key':key5,
    'room 6 key':key6,
    'room 7 key':key7,
    'room 8 key':key8,
}

keys=[key1,key2,key3,key4,key5,key6,key7,key8]