#!/usr/bin/env python3

from rooms import *
"""
Map class used to build a map from all of the rooms
"""



class Map():

    def __init__(self, rooms = {}):
        self.rooms = rooms


    def __repr__(self):
        return "Map: {}".format(self.rooms)







def build_map(id, num_of_rooms):
    rooms = {}
    room_count = 0
    while room_count < num_of_rooms:
        rooms[id] = get_room(id)
        id += 1
        room_count += 1
    return rooms
start_id = 1
num_rooms = 3
a_map = Map(build_map(start_id, num_rooms))
