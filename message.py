######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: RPG - Inventory
# Coder: Suri Ho
# Version: 3.0
######################################################################
''' Instructions and story line for the game so user knows the goal'''
######################################################################
# Imports
import inventory

# Instructions for the game
def instructions():
    ''' The function will print out the instructions for player.'''
    print("Welcome to the mansion!")
    print("It belonged to your grandfather, who lived alone and"\
          " has just passed away.")
    print("You heard that he hide some treasures here, so with a given"\
          " hint, you attempt to find them.")
    print("You can type 'quit' to exit the game at any point.\n")
    print("Hints will be saved in inventory. Here's your hint."\
          " Good luck!")
    print(inventory.hints["hint1"]["description"])
    inventory.inventory.append("hint1")