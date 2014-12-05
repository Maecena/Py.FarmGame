import random

from items import *

class ForestLocation(object):
    def __init__(self, items):
        self.items = items

    def search(self):
        return random.choice(self.items)

wild = ForestLocation([blueberry, blueberry, apple, \
                       apple, vine, onion, ginger, strawberry, strawberry, mint])
bridge = ForestLocation([stone, shijemi, pebbles, \
                         pebbles, pebbles, vine, vine])
hut = ForestLocation([twig, twig, shijemi, branch, \
                      branch, branch, branch, bark, bark])
bog =  ForestLocation([twig, blueberry, vine, vine, twig, dirt])
mine = ForestLocation([sand, sand, sand, pebbles, \
                       pebbles, dirt, stone, stone, stone])


