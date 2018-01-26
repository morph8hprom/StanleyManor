#!/usr/bin/env python3

"""
Item class defining template for items and function to load item
data from json file
"""

class Item():
    def __init__(self, id = 0, name = "", desc = ""):
        self.id = id
        self.name = name
        self.desc = desc

def get_items(id):
    """
    Function to load item data from json files
    """
    ret = None
    with open("data/item/item{}.json".format(str(id)) , "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext, strict = False)
        d['id'] = id
        ret = Item(**d)
    return ret
