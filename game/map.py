#!/usr/bin/env python3

from rooms import *
"""
Map class used to contain the map of all of the rooms and a fucntion for
building the map.
"""



class Map():

    def __init__(self, rooms = {}):
        self.rooms = rooms


    def __repr__(self):
        return "Map: {}".format(self.rooms)







def build_map(id, num_of_rooms):
    """
    Function used to build the map.
    Takes the starting id and max number of rooms as parameters
    """
    rooms = {}
    room_count = 0
    while room_count < num_of_rooms:
        rooms[id] = get_room(id)
        id += 1
        room_count += 1
    return rooms
