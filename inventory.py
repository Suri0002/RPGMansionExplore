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
import sys
import character
import map

# Hints database
hints = {
    "hint1": {
        "description": "I treasured it the most but I can't have it. What's it?",
        "action": ["view", "answer"]
    },
    "hint2": {
        "description": "Please take good care of my bird",
        "action": ["view"]
    },
    "hint3": {
        "description": "Two people walk in the night, whispering a story."\
        " The Queen is free and leaves behind her roses. The King is trapped"\
        " in his throne. And the Knight keeps crossing the forest but finds"\
        " nothing.",
        "action": ["view"],
        "status": []
    }
}

# Items database
items = {
    "book": {
        "description": "Looks like there's a piece of paper stuck inside.",
        "location": None,
        "action": ["open"]
    },
    "drinking bird": {
        "description": "You find a drinking bird on the table, standing next"\
        " to an arrow pointing to the right bookcase. Looks like you have to"\
        " take care of this bird!",
        "location": "office",
        "action": [None],
        "status": []
    },
    "cup": {
        "description": "You find a glass cup on the counter.",
        "location": "kitchen",
        "action": ["keep", "fill", "place"],
        "status": []
    },
    "clock": {
        "description": "You find a suspicious clock on the wall.",
        "location": "living room",
        "action": ["answer"]
    }
}

inventory = []

# Functions


def viewInventory():
    ''' '''
    if inventory:
        print("Inventory: ")
        for item in inventory:
            print(f"*{item}")
    else:
        print("You have nothing in your inventory.")


def useInventory():
    ''' '''
    choosing = True
    item_choice = input("Choose an item: ").lower()
    while choosing:
        if item_choice == "hint1":
            for action in hints["hint1"]["action"]:
                print(f"*{action}")
            print("*done")
            item_action = input("What do you want to do? ").lower()
            if item_action == "view":
                print(hints["hint1"]["description"])
            elif item_action == "quit":
                sys.exit("Thank you for playing!")
            elif item_action == "done":
                choosing = False
            elif item_action == "answer":
                answer = input("Please type your answer: ").lower()
                if answer == "family":
                    inventory.append("hint2")
                    print("You've found the second hint!")
                    print(hints["hint2"]["description"])
                else:
                    print("That's not the answer.")
            else:
                print("Invalid choice. Try again.")
                choosing = False
        if item_choice == "hint2" or item_choice == "hint3":
            for action in hints["hint2"]["action"]:
                print(f"*{action}")
            print("*done")
            item_action = input("What do you want to do? ").lower()
            if item_action == "view":
                print(hints["hint2"]["description"])
            elif item_action == "quit":
                sys.exit("Thank you for playing!")
            elif item_action == "done":
                choosing = False
            else:
                print("Invalid choice. Try again.")
        if item_choice == "cup":
            #for action in items["cup"]["action"]:
                #print(f"*{action}")
            #print("*done")
            #item_action = input("What do you want to do? ").lower()
            cupAction()
        else:
            print("Invalid choice. Try again.")
            choosing = False


def inspect_Room():
    ''' '''
    global object, location_
    object_found = False
    room_inventory = []
    location_ = map.mansion_map[character.yloc][character.xloc]
    for object in items:
        object_loc = items[object]["location"]
        if object_loc == location_:
            print(items[object]["description"])
            object_found = True
            room_inventory.append(object)
    if object_found is True:
        for item in room_inventory:
            if item == "drinking bird":
                birdAction()
            elif item == "cup":
                cupAction()
            elif item == "clock":
                clockAction()
    else:
        print("There is nothing suspicious in the room.")


def cupAction():
    ''' '''
    choosing = True
    while choosing:
        for action in items["cup"]["action"]:
            print(f"*{action}")
        print("*done")
        cup_choice = input("Choose an action: ").lower()
        if cup_choice == "keep":
            inventory.append("cup")
            print("Cup is now in your inventory.")
            items["cup"]["action"] = items["cup"]["action"].pop("keep")
        elif cup_choice == "quit":
            sys.exit("Thank you for playing!")
        elif cup_choice == "done":
            choosing = False
        elif cup_choice == "fill":
            print("You've filled the cup with water")
            items["cup"]["action"] = items["cup"]["action"].pop("fill")
            items["cup"]["status"] = items["cup"]["status"].append("filled")
        elif cup_choice == "place":
            if location_ == "office":
                print("Cup is place in front of the arrow, next to the bird.")
                items["cup"]["status"] = items["cup"]["status"].append("placed")
            else:
                print("You can't place it here!")
        else:
            print("Invalid choice. Try again.")


def birdAction():
    ''' '''
    if items["cup"]["status"] == "filled" and "placed":
        print("The bird is drinking water. You've taken care of it.")
        print("Looks like the arrow is pointing at the big book beside,"\
             " not the bookcase.")
        items["drinking bird"]["status"] = "cared"
    else:
        print("You can't do anything with the bird now." + "\n")


def bookAction():
    ''' '''
    if items["drinking bird"]["status"] == "cared":
        print(items["book"]["description"])
        choosing = True
        while choosing:
            for action in items["book"]["action"]:
                print(f"*{action}")
            print("*done")
            book_choice = input("Choose an action: ").lower()
            if book_choice == "open":
                print("You've found the last hint: ")
                print(hints["hint3"])
                inventory.append("hint3")
                print("Hint is save in inventory.")
                hints["hint3"]["status"] = hints["hint3"]["status"].append("active")
                choosing = False
            elif book_choice == "quit":
                sys.exit("Thank you for playing!")
            elif book_choice == "done":
                choosing = False
            else:
                print("Invalid choice. Try again.")


def clockAction():
    ''' '''
    if hints["hint3"]["status"] == "active":
        print("Looks like you have to rotate its hands in the correct order."\
              " Choose answer and type the numbers you think are right in.")
        choosing = True
        while choosing:
            for action in items["clock"]["action"]:
                print(f"*{action}")
            print("*done")
            clock_choice = input("Choose an action: ").lower()
            if clock_choice == "answer":
                answer = input("Please type your answer: ").lower()
                if answer == "0, 9, 0, 3":
                    print("The clock is the key to open the safe box hidden"\
                          " inside the fireplace.")
                    print("Congrats you found the property and successfully"\
                          " inherited them.")
                    sys.exit("Thank you for playing!")
                else:
                    print("That's not the answer.")
            elif clock_choice == "quit":
                sys.exit("Thank you for playing!")
            elif clock_choice == "done":
                choosing = False
            else:
                print("Invalid choice. Try again.")
    else:
        print("You can't do anything with it now." + "\n")