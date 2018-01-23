#!usr/bin/env python3

"""
A room class and a method to load room data from json files
"""




import json


class Room():
    def __init__(
        self,
        id = "0",
        name = "An empty room",
        desc = "There is nothing here",
        items = {},
        exits = {},
        ):
        self.id = id
        self.name = name
        self.desc = desc
        self.items = items
        self.exits = exits
    def __repr__(self):
        return "{}\n{}\n{}\n{}\n".format(self.name, self.desc, self.items, self.exits)

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

# Create method to get room info from json file
def get_room(id):
    ret = None
    with open("data/room/room{}.json".format(str(id)) , "r") as f:
        jsontext = f.read()
        d = json.loads(jsontext, strict = False)
        d['id'] = id
        ret = Room(**d)
    return ret
