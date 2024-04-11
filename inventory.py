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
        "description": "You will see that in my eye",
        "location": None
    },
    "hint2": {
        "description": "Please take good care of my bird",
        "location": "gallery"
    },
    "hint3": {
        "description": "",
        "location": "office"
    },
    "table mirror": {
        "description": "",
        "location": "living room"
    },
    "paintings": {
        "description": "",
        "location": "gallery"
    },
    "family photos": {
        "description": "",
        "location": "gallery"
    },
    "sculpture": {
        "description": "",
        "location": "main hall"
    },
    "clock": {
        "description": "",
        "location": "living room"
    }
}