######################################################################
# Title: RPG_Mansion Map
# Class: CS 30
# Assignment: Data Structures: RPG - Map
# Coder: Suri Ho
# Version: 1.0
######################################################################
''' 
'''
######################################################################

mansion_map = [
    ["living room", "office", "bedroom"],
    ["main hall", "hallway", "hallway"],
    ["gallery", "dining room", "kitchen"]
]

# Mansion rooms database
mansion_rooms = {
    "bedroom": {
        "description": "Across the room is a door open to a balcony. On the"\
        " right are a bed and a lamp on the bedside table. On the left is a"\
        " wooden wardrobe.",
        "options": ["south"]
    },
    "office": {
        "description": "There are two bookcases on two sides of the walls,"\
        " filled with books and other collections. In the middle, an office"\
        " table and chair, with a large window behind.",
        "options": ["south"]
    },
    "main hall": {
        "description": "On the left is a living room. On the right is a gallery.",
        "options": ["north", "south"]
    },
    "hallway": {
        "description": "There are old paintings hang on the walls",
        "options": ["north", "east", "south", "west"]
    },
    "living room": {
        "description": "Across the room, a large stone fireplace stands between"\
        " two big windows. On its shelf is a table mirror. In the middle are"\
        " two couches facing each other, with a long coffee table between.",
        "options": ["south"]
    },
    "gallery": {
        "description": "On the wall are your grandfather’s paintings, with"\
        " several family photos. Beside that, it is an empty room.",
        "options": ["left"]
    },
    "dining room": {
        "description": "Dining room has a long table in the middle. Chairs are"\
        " stacked at the right corner. Across the room are two large windows,"\
        " with the white curtains open. Between them hangs an old painting. The"\
        " door on the right connects with the kitchen.",
        "options": ["north", "east"]
    },
    "kitchen": {
        "description": "On the left are the oven, stove, cabinets, drawers and"\
        " sink. A big fridge on the left corner. In the middle is a long table."\
        " The door on the left connects to the dining room.",
        "options": ["north", "west"]
    },
}

Player = {"yloc": 1, "xloc": 0}

# Functions


def current_loc():
    ''' '''
    if Player["yloc"] > 2 and Player["xloc"] > 2:
        print("You can't move further")
    else:
        playerloc = mansion_map[Player["yloc"]][Player["xloc"]]
        print(f"You're in {playerloc}.\n {mansion_rooms[playerloc]}")
    

def direction():
    ''' '''
    north_move()
    south_move()
    east_move()
    west_move()


def north_move():
    ''' '''
    if move.lower() == "north":
        Player["yloc"] = Player["yloc"]-1
    current_loc()


def south_move():
    ''' '''
    if move.lower() == "south":
        Player["yloc"] = Player["yloc"]+1
    current_loc()


def east_move():
    ''' '''
    if move.lower() == "east":
        Player["xloc"] = Player["xloc"]+1
    current_loc()


def west_move():
    ''' '''
    if move.lower() == "west":
        Player["xloc"] = Player["xloc"]-1
    current_loc()


def player_choice():
    ''' '''
    global move
    current_loc()
    while True:
        move = input("Which direction do you want to go? ")
        direction()


player_choice()
            