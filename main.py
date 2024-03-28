######################################################################
# Title: RPG_Mansion Map
# Class: CS 30
# Assignment: Data Structures: RPG - Map
# Coder: Suri Ho
# Version: 1.0
######################################################################
''' The program allows player to choose an action at the start. If 
they choose to go around, they will be given a description of the room
they are currently in, and the direction options. Player then decide a 
direction they want to travel. If player choose to quit, the program 
will stop.
'''
######################################################################
# Import
import sys

# Mansion map array
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
        "description": "There is a medium plaster sculpture in the middle.",
        "options": ["north", "south", "east"]
    },
    "hallway": {
        "description": "There are old paintings hanging on the walls",
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
        "options": ["north"]
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

# Player dictionary
Player = {"yloc": 1, "xloc": 0}

# Valid action
actions = ["go", "quit"]
# Functions


def current_loc():
    ''' The function will updated on player location and print out their 
    current room's description and direction options.
    '''
    global playerloc
    # Player location will be updated based on user choice
    playerloc = mansion_map[Player["yloc"]][Player["xloc"]]
    # Print player location with description and direction options
    print(f"You're in {playerloc}.")
    print(mansion_rooms[playerloc]["description"] + "\n")
    print("Direction option(s): ")
    for option in mansion_rooms[playerloc]["options"]:
        print(f"* {option}")
    print("\n")


def direction():
    ''' The function will update player's location on the row or
    column in the map based on their direction choice. The location
    will only be updated if the direction is in their current room's
    options. If the chosen direction is not in their room's options,
    an invalid message will be print and player need to choose a valid
    option offered.
    '''
    if way in mansion_rooms[playerloc]["options"]:
        if way == "north":
            Player["yloc"] = Player["yloc"] - 1
        elif way == "south":
            Player["yloc"] = Player["yloc"] + 1
        elif way == "east":
            Player["xloc"] = Player["xloc"] + 1
        elif way == "west":
            Player["xloc"] = Player["xloc"] - 1
        else:
            # Invalid message if user type a different input
            # than 'north', 'south', 'west', 'east'
            print("Invalid direction!\n")
        current_loc()
    else:
        print("You can't go that way." + "\n")


def player_location():
    ''' The function will ask for a direction from user, then update
    their location based on the choice. If player choose 'quit', the
    program will stop.
    '''
    global way
    while True:
        # Print out current location so player know where they are at
        current_loc()
        way = input("Which direction do you want to go? ").lower()
        print("\n")
        if way == "quit":
            sys.exit("Thank you for playing!")
        else:
            # Go to direction() function to update player location
            direction()
            break


def player_action():
    ''' The function will print out actions that player can do and ask for 
    an action input, then execute based on the choice. If player choose 
    'quit', the program will stop.
    '''
    while True:
        for action in actions:
            print(action)
        move = input("What do you want to do? ").lower()
        print("\n")
        if move not in actions:
            print("Invalid action!\n")
        if move == "quit":
            sys.exit("Thank you for playing!")
        if move == "go":
            player_location()


def instructions():
    ''' The function will print out the instructions for player.'''
    print("Welcome to the mansion!\n")
    print("You can type 'quit' to exit the game at any point.\n")


def main():
    ''' The function calls other function to execute the code'''
    instructions()
    player_action()


# Main
main()