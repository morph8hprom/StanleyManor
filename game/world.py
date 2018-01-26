#!/usr/bin/env python3
from map import *
from player import *
from items import *
"""
World class defining template for world and function used to
generate world, taking map, player, and items arguments.
"""
class World():
    """
    Defines the template for the world
    """


    def __init__(self, game_map, game_player, game_items):
        self.game_map = game_map
        self.name = "Stanley Manor"
        self.game_player = game_player
        self.items = game_items


    def __repr__(self):
        return "NAME:{}\nMAP:{}".format(self.name, a_map.rooms)






def build_world(game_map, game_player, game_items):
    """
    Function to build world.  Takes map, player, and items as arguments
    """
    a_world = World(game_map, player, items)
    return a_world
start_id = 1
num_rooms = 3
a_map = Map(build_map(start_id, num_rooms))
a_world = build_world(a_map)
