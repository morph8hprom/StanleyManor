#!/usr/bin/env python3
from map import *
from player import *
from items import *
from world import *

"""
File containing main game logic
"""


def intro():
    """
    Function for introduction.
    """
    pass
def char_select():
    """
    Function for character selection
    """
    pass



def main():
    start_id = 1
    num_rooms = 3
    a_map = Map(build_map(start_id, num_rooms))
    a_player = Player(get_player)
    a_world = build_world(a_map, a_player, game_items)
