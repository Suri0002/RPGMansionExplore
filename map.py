######################################################################
# Title: RPG_Mansion Map
# Class: CS 30
# Assignment: External Files: RPG - Try/Except
# Coder: Suri Ho
# Version: 2.0
######################################################################
''' This program will write a map to an external file, read the file
and then print out the map.
''' 
######################################################################
# Import
from tabulate import tabulate

# Mansion map array
mansion_map = [
    ["living room", "office", "bedroom"],
    ["main hall", "hallway", "hallway"],
    ["gallery", "dining room", "kitchen"]
]

# Mansion rooms database
mansion_rooms = {
    "bedroom": {
        "description": "Across the room, a door open to a balcony. On the"\
        " right are a bed and a bedside table. On the left is a wooden wardrobe.",
        "options": ["south"]
    },
    "office": {
        "description": "It's an organized office with a huge collection of books",
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
        " two big windows. In the middle are two couches facing each other, with a"\
        " long coffee table in between.",
        "options": ["south"]
    },
    "gallery": {
        "description": "On the wall are your grandfather’s paintings beside some"\
        " family photos.",
        "options": ["north"]
    },
    "dining room": {
        "description": "Dining room has a long table in the middle. Chairs are"\
        " stacked at the right corner. Across the room are two large windows"\
        " and an old painting hung in between.",
        "options": ["north", "east"]
    },
    "kitchen": {
        "description": "It is a clean kitchen that hasn't been used for a long time.",
        "options": ["north", "west"]
    },
}

# Map external file
mapfile = 'map.txt'

#Functions


def WriteMap():
    ''' The function will write map to an external file'''
    try:
        with open(mapfile, "w") as file:
            file.write(tabulate(mansion_map, tablefmt = "simple_grid"))
    except:
        print("Oops! Can't write to file")
    else:
        print("Mansion map has been created.")
    finally:
        print("Let's explore!")


def ReadMap():
    ''' The function will read a file and print out the map'''
    try:
        with open(mapfile, "r") as file:
            print(file.read())
    except:
        print("Map can't be read!")
    else:
        print("Here is the map of this mansion!")
    finally:
        print("Good luck!!" + "\n")


def showMap():
    ''' The function will call the function that writes map to an 
    external file and function that reads and prints out the map 
    '''
    WriteMap()
    ReadMap()