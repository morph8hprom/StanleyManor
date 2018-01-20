# -*- coding: utf-8 -*-
from sys import exit
# Create a class defining the basics of a scene
class Scene(object):

    def __init__(self, ID = None, desc = '', inter = [], exits = []):
        self.ID = None
        self.desc = ''
        self.inter= []
        self.exits = []

    # Create a string method to view the parameters of a scene
    def __str__(self):
        line = "-" * len(self.ID)
        return "{}\n{}\n{}\n{}\n{}".format(self.ID, line, self.desc, self.inter, self.exits)

    # Create a method to print the description of the scene and exits.
    def print_desc(self):
        print self.desc
        # Creates a string from the list of exits
        print ','.join(map(str, self.exits))


# Create a class for the game engine
class Engine(object):

    def __init__(self, )
