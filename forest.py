import random

from items import *

class ForestLocation(object):
    def __init__(self, items):
        self.items = items

    def search(self):
        return random.choice(self.items)

wild = ForestLocation([blueberry, blueberry, pebbles])
bridge = ForestLocation([stone, shijemi, pebbles, pebbles, pebbles])
hut = ForestLocation([twig, twig, shijemi, branch, bark, bark])
bog =  ForestLocation([twig, blueberry, twig, dirt])
