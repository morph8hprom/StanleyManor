#!/usr/bin/env python3

from map import *

"""
A player class defining template for player and function to load player
data from json file.
"""

class Player():
    def __init__(self, id = 0,  name = "", desc = " ", loc = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.loc = loc

    def move(self, loc):
        pass


def get_player(id):
    """
    Function to load player data from json files
    """
    ret = None
    with open("data/player/player{}.json".format(str(id)) , "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext, strict = False)
        d['id'] = id
        ret = Player(**d)
    return ret
