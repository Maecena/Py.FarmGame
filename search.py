import random
import player as player

#places = wild , bridge , hut , bog

wild_search = ['blueberry', 'blueberry', 'pebbles']
bridge_search = ['stone', 'shijemi', 'pebbles', 'pebbles', 'pebbles']
hut_search = ['twig', 'twig', 'shijemi', 'branch', 'bark', 'bark']
bog_search = ['twig', 'blueberry', 'twig', 'dirt']


class gather(object):
    def __init__(self, items):
        self.items = items

    def find(self):
        found = random.choice(self.items)
        print ("You found a " + str(found) + "!")
        player.pc.add_inv(found)
        return

wild = gather(wild_search)
bridge = gather(bridge_search)
hut = gather(hut_search)
bog =  gather(bog_search)
