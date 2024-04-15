######################################################################
# Title: RPG_Mansion Explore
# Class: CS 30
# Assignment: RPG - Inventory
# Coder: Suri Ho
# Version: 3.0
######################################################################
''' '''
######################################################################

# Mansion map array
mansion_map = [
    ["living room", "office", "bedroom"],
    ["main hall", "hallway", "hallway"],
    ["gallery", "dining room", "kitchen"]
]

# Items database
items = {
    "hint1": {
        "description": "Once there is a break, it shatters. I've tried"\
        " my best to keep, but I can't clue the pieces together.",
        "action": ["keep"]
    },
    "hint2": {
        "description": "Please take good care of my bird",
        "action": ["keep"]
    },
    "hint3": {
        "description": "Two people walk in the night, whispering a story."\
        " The Queen is free and leaves behind her roses. The King is trapped"\
        " in his throne. And the Knight keeps crossing the forest but finds"\
        " nothing.",
        "action": ["keep"]
    },
    "book": {
        "description": "Looks like there's a piece of paper stuck inside.",
        "location": "office",
        "action": ["open"]
    },
    "drinking bird": {
        "description": "Looks like you have to take care of this bird.",
        "location": "office",
        "action": [None]
    },
    "cup": {
        "description": "You find a glass cup.",
        "location": "kitchen",
        "action": ["keep", "fill", "place"]
    }
}

inventory = []

# Functions


def viewInventory():
    if inventory:
        print("Inventory: ")
        for item in inventory:
            print(f"*{item}")
    else:
        print("You have nothing in your inventory.")


