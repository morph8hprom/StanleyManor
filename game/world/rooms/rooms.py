# Define room class
# Create method to load data from json files


#!usr/bin/env python3

import json
class Room():
    def __init__(
        self,
        id = "0",
        name = "An empty room",
        desc = "There is nothing here"
        items = {}
        exits = {}
        ):
        self.id = id
        self.name = name
        self.desc = desc
        self.items = items
        self.exits = exits

    # Create method to get room info from json file
    def get_room(id):
        ret = None
        with open(str(id))+".json" , "r") as f:
            jsontext = f.read()
            d = json.loads(jsontext)
            d['id'] = id
            ret = Room(**d)
    # Create method to verify exits
    def _exits(self, dir):
        if dir in self.exits:
            return self.exits[dir]
        else:
            return None

    def north(self):
        return self._exits('n')

    def south(self):
        return self._exits('s')

    def east(self):
        return self._exits('e')

    def west(self):
        return self._exits('w')
