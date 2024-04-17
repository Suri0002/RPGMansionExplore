######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: RPG - Inventory
# Coder: Suri Ho
# Version: 3.0
######################################################################
''' '''
######################################################################
# Imports
import inventory

# Instructions for the game
def instructions():
    ''' The function will print out the instructions for player.'''
    print("Welcome to the mansion!")
    print("It belonged to your grandfather. He lived here alone and"\
          " has just passed away.")
    print("He left behind his huge property, and a hint. If you could"\
          " find where he hide it, it will be yours.")
    print("You can type 'quit' to exit the game at any point.\n")
    print("Hints will be saved in inventory. Here's your hint."\
          " Good luck!")
    print(inventory.hints["hint1"]["description"])
    inventory.inventory.append("hint1")