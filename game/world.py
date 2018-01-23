#!/usr/bin/env python3
from map import *
from player import *
from items import *

class World():



    def __init__(self, game_map):
        self.game_map = game_map
        self.name = "Stanley Manor"

    def __repr__(self):
        return "NAME:{}\nMAP:{}".format(self.name, a_map.rooms)





    

def build_world(game_map):
    a_world = World(game_map)
    return a_world

a_world = build_world(a_map)
