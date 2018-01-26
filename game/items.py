#!/usr/bin/env python3

"""
Item class defining template for items and function to load item
data from json file
"""

class Item():
    """
    Defines the template for items
    """
    def __init__(self, id = None, name = "", desc = ""):
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

def item_list(id, num_of_items):
    """
    Function used to generate item list using get_items function
    """
    items = {}
    item_count = 0
    while item_count < num_of_items:
        items[id] = get_items(id)
        id += 1
        item_count += 1
    return items
