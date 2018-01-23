#!/usr/bin/env python3
from map import *
from player import *
from items import *
from world import *

class Engine():
    def __init__(self, game_world):
        self.game_world = game_world

    def game_loop(self):
        pass
    def intro(self):
        print("Welcome!  Press enter to begin")

def build_engine(game_world):
    game_engine = Engine(game_world)
    return game_engine

a_engine = build_engine(a_world)
