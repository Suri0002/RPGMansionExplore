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
        "location": None
    },
    "hint2": {
        "description": "Please take good care of my bird",
        "location": "gallery"
    },
    "hint3": {
        "description": "Two people walk in the night, talking about a story."\
        " The Queen is free and leaves behind her roses. The King is trapped"\
        " in his throne. And the Knight keeps crossing the forest but finds"\
        " nothing.",
        "location": "book"
    },
    "cup": {
        "description": ""
    }
}