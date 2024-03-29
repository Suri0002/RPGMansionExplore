######################################################################
# Title: RPG_Mansion Map
# Class: CS 30
# Assignment: External Files: RPG - Try/Except
# Coder: Suri Ho
# Version: 2.0
######################################################################
''' 
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

# Map external file
mapfile = 'map.txt'

#Functions


def WriteMap():
    ''' '''
    try:
        with open(mapfile, "w") as file:
            file.write(tabulate(mansion_map, tablefmt = "simple_grid"))
    except:
        print("Oops! Can't write to file")
    else:
        print("Mansion map has been created.")
    finally:
        print("Good luck!")


def ReadMap():
    ''' '''
    try:
        with open(mapfile, "r") as file:
            print(file.read())
    except:
        print("Map can't be read!")
    else:
        print("Here is the map of this mansion!")
    finally:
        print("Good luck")


def showMap():
    WriteMap()
    ReadMap()


# Main
showMap()