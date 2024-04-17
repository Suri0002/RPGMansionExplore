######################################################################
# Title: RPG_Mansion Map
# Class: CS 30
# Assignment: Data Structures: RPG - Map
# Coder: Suri Ho
# Version: 2.0
######################################################################
''' The program allow player to view map and go around the mansion.
Player can choose to quit the game at any point.
'''
######################################################################
# Imports
import sys
import character
import inventory
import map
import message

# Valid action
actions = ["go", "quit", "map", "look", "inventory"]

# Functions


def current_loc():
    ''' The function will updated on player location and print out their 
    current room's description.
    '''
    global playerloc
    #Player location will be updated based on user choice
    playerloc = map.mansion_map[character.yloc][character.xloc]
    # Print player location with description
    print(f"You're in {playerloc}.")
    print(map.mansion_rooms[playerloc]["description"])


def movement():
    ''' The function will update player's location on the row or
    column in the map based on their direction choice. The location
    will only be updated if the direction is in their current room's
    options. If the chosen direction is not in their room's options,
    an invalid message will be print and player need to choose a valid
    option offered.
    '''
    if way in map.mansion_rooms[playerloc]["options"]:
        if way == "north":
            character.yloc = character.yloc - 1
        elif way == "south":
            character.yloc = character.yloc+ 1
        elif way == "east":
            character.xloc = character.xloc + 1
        elif way == "west":
            character.xloc = character.xloc - 1
        else:
        # Invalid message if user type a different input
        # than 'north', 'south', 'west', 'east'
            print("Invalid direction!\n")
    else:
        print("You can't go that way." + "\n")



def player_location():
    ''' The function will ask for a direction from user, and update
    their location based on the choice. If player choose 'quit', the
    program will stop.
    '''
    global way
    print("Direction option(s): ")
    for option in map.mansion_rooms[playerloc]["options"]:
        print(f"* {option}")
    while True:
        way = input("Which direction do you want to go? ").lower()
        print("\n")
        if way == "quit":
            sys.exit("Thank you for playing!")
        else:
            # Go to direction() function to update player location
            movement()
            break
            

def player_action():
    ''' The function will print out actions that player can do and ask for 
    an action input, then execute based on the choice. If player choose 
    'quit', the program will stop.
    '''
    while True:
        current_loc()
        for action in actions:
            print(f"-{action}")
        move = input("What do you want to do? ").lower()
        print("\n")
        if move not in actions:
            print("Invalid action!\n")
        if move == "quit":
            sys.exit("Thank you for playing!")
        if move == "go":
            player_location()
        if move == "map":
            map.showMap()
        if move == "look":
            inventory.inspect_Room()
        if move == "inventory":
            inventory.viewInventory()


def main():
    ''' The function calls other function to execute the code'''
    message.instructions()
    player_action()


# Main
main()