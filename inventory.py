######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: RPG - Inventory
# Coder: Suri Ho
# Version: 3.0
######################################################################
''' The program allows player to interact with their inventory and
look for interactive objects in rooms. Player can choose quit to stop.
'''
######################################################################
# Imports
import sys
import character
import map

# Hints database
hints = {
    "hint1": {
        "description": "Please take good care of my bird",
        "action": ["view", "done"]
    },
    "hint2": {
        "description": "Two people walk in the night, whispering a story."\
        " The Queen is free and leaves behind her roses. The King is trapped"\
        " in his throne. And the Knight keeps crossing the forest but finds"\
        " nothing.",
        "action": ["view", "done"],
        "status": "waiting"
    }
}

# Items database
items = {
    "book": {
        "description": "Looks like there's a piece of paper stuck inside.",
        "location": None,
        "action": ["open", "done"]
    },
    "drinking bird": {
        "description": "You find a drinking bird on the table, standing next"\
        " to an arrow pointing to the right bookcase.",
        "location": "office",
        "action": [None],
        "status": []
    },
    "cup": {
        "description": "You find a glass cup on the counter.",
        "location": "kitchen",
        "action": ["fill", "place", "done"],
        "status1": "waiting",
        "status2": "waiting"
    },
    "clock": {
        "description": "You find a suspicious clock on the wall.",
        "location": "living room",
        "action": ["answer", "done"]
    }
}
# User's inventory
inventory = []

# Functions


def viewInventory():
    ''' The function will trigger when user chooses inventory in the
    main menu. User will be asked if they want to access any item in
    the inventory. If they choose yes, action for chosen item will 
    perform. If they choose no, they will return to main menu. Player
    can choose quit to stop.
    '''
    choosing = True
    while choosing:
        if inventory:
            print("Inventory: ")
            for item in inventory:
                print(f"*{item}")
            access_choice = input("Do you want to access any item? ").lower()
            if access_choice == "quit":
                sys.exit("Thank you for playing!")
            if access_choice == "yes":
                useInventory()
            elif access_choice == "no":
                choosing = False
            else:
                print("Please choose yes or no.")
        else:
            print("You have nothing in your inventory.")


def useInventory():
    ''' The function will trigger when player want to access items
    in inventory. It call other functions depend on what
    item player chooses to access. Player can choose quit to stop.
    '''
    global item_choice
    choosing = True
    while choosing:
        item_choice = input("Choose an item: ").lower()
        if item_choice not in inventory:
            print("Please choose an item in inventory.")
        if item_choice == "quit":
            sys.exit("Thank you for playing!")
        if item_choice == "hint1" or item_choice == "hint2":
            hintAction()
            choosing = False
        elif item_choice == "cup":
            cupAction()
            choosing = False


def inspect_Room():
    ''' The function will trigger when user choose 'look'. If there is
    an object at their location, description will be printed. If there
    is no interactive piece, a message will be printed.
    '''
    global object, location_
    object_found = False
    room_inventory = []
    location_ = map.mansion_map[character.yloc][character.xloc]
    for object in items:
        object_loc = items[object]["location"]
        # Print item's description if it's at player's current location
        if object_loc == location_:
            print(items[object]["description"])
            object_found = True
            room_inventory.append(object)
    if object_found is True:
        for item in room_inventory:
            if item == "drinking bird":
                birdAction()
            elif item == "cup":
                cupChoice()
            elif item == "clock":
                clockAction()
    else:
        print("There is nothing suspicious in the room.")


def hintAction():
    ''' The function let user to interact with hints in their inventory.
    Player can choose quit to stop.
    '''
    choosing = True
    while choosing:
        for action in hints[item_choice]["action"]:
            print(f"*{action}")
        item_action = input("What do you want to do? ").lower()
        if item_action not in hints[item_choice]["action"]:
            print("Invalid action for hint.")
        if item_action == "view":
            print(hints[item_choice]["description"])
        elif item_action == "quit":
            sys.exit("Thank you for playing!")
        elif item_action == "done":
            choosing = False


def cupChoice():
    ''' The function will ask player if they want to keep the item
    or not. Player can choose quit to stop.
    '''
    choosing = True
    while choosing:
        # Print options to add the cup into inventory
        print("*keep")
        print("*done")
        cup_choice = input("Choose an action: ").lower()
        if cup_choice == "keep":
            inventory.append("cup")
            print("Cup is now in your inventory.")
            choosing = False
        elif cup_choice == "quit":
            sys.exit("Thank you for playing!")
        elif cup_choice == "done":
            choosing = False
        else:
            print("Invalid choice. Try again.")


def cupAction():
    ''' The function will trigger only if the cup is in inventory.
    Player can choose to fill or place the cup, which will be useful
    to solve for hint. Player can choose quit to stop.
    '''
    choosing = True
    while choosing:
        for action in items["cup"]["action"]:
            print(f"*{action}")
        cup_action = input("What do you want to do? ").lower()
        if cup_action not in items["cup"]["action"]:
            print("You can't do that with the cup.")
        if cup_action == "done":
            choosing = False
        elif cup_action == "fill":
            print("You've filled the cup with water")
            # Change one status to filled
            items["cup"]["status1"] = "filled"
        elif cup_action == "place":
            # Cup can only be placed if player is in the office
            if location_ == "office":
                print("Cup is place in front of the arrow, next to the bird.")
                # Change one status to placed
                items["cup"]["status2"] = "placed"
            else:
                print("You can't place it here!")


def birdAction():
    ''' The function will lead player to another hint only after player has
    fill and place the cup in the office. Before that, player can't do any
    thing with the bird. 
    '''
    # If both cup's status changed, player will be inform that hint
    # is in the book
    if items["cup"]["status1"] == "filled":
        if items["cup"]["status2"] == "placed":
            print("The bird is drinking water. You've taken care of it.")
            print("Looks like the arrow is pointing at the big book on"\
                  " the left, not the bookcase.")
            items["drinking bird"]["status"] = "cared"
            bookAction()
    else:
        print("You can't do anything with the bird now." + "\n")


def bookAction():
    ''' The function will print another hint if player has completed
    taking care of the bird and open the book. Player can choose quit
    to stop.
    '''
    if items["drinking bird"]["status"] == "cared":
        print(items["book"]["description"])
        choosing = True
        while choosing:
            for action in items["book"]["action"]:
                print(f"*{action}")
            book_choice = input("Choose an action: ").lower()
            if book_choice not in items["book"]["action"]:
                print("You can't do that with the book.")
            # Print the second hint when player choose to open the book
            if book_choice == "open":
                print("You've found the another hint: ")
                print(hints["hint2"]["description"])
                inventory.append("hint2")
                print("Hint is saved in inventory.")
                hints["hint2"]["status"] = "active"
                choosing = False
            elif book_choice == "quit":
                sys.exit("Thank you for playing!")
            elif book_choice == "done":
                choosing = False


def clockAction():
    ''' The function will let the player interact with the clock after they
    have found the second hint. Player need to answer correctly to win. Player
    can choose quit to stop.
    '''
    # Instruction to interact with the clock will be printed after player
    # has found the second hint
    if hints["hint2"]["status"] == "active":
        print("You realized that you have to rotate its hands four times in"\
              " the correct order.")
        choosing = True
        while choosing:
            for action in items["clock"]["action"]:
                print(f"*{action}")
            clock_choice = input("Choose an action: ").lower()
            if clock_choice not in items["clock"]["action"]:
                print("You can't do that with the clock.")
            if clock_choice == "answer":
                answer = input("Enter the hours you want to rotate to: ").lower()
                if answer == "0, 9, 0, 3":
                    print("The clock is the key to open the safe box hidden"\
                          " inside the fireplace.")
                    print("Congrats you found the treasures.")
                    sys.exit("Thank you for playing!")
                else:
                    print("That's not the answer.")
            elif clock_choice == "quit":
                sys.exit("Thank you for playing!")
            elif clock_choice == "done":
                choosing = False
    else:
        print("You can't do anything with it now." + "\n")