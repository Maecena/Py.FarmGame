import random
from collections import defaultdict

from items import *
from clock import gameTime



class Player(object):
    def __init__(self, exp, money, actions, actionCount):
        self.exp = exp
        self.lvl = 0
        self.money = money
        self.inventory = Inventory()
        self.actions = actions
        self.actionCount = actionCount

    def printStats(self):
        return (str(self.money), str(self.lvl), str(self.exp))

    def expGain(self, num=1):
        self.exp += num
        lvlup = 100
        if self.exp >= lvlup:
            self.lvl += 1
            self.exp -= lvlup
            lvlup = lvlup * 1.1
            if (self.lvl % 2 == 0):
                addActions(1)
        
    #updates the count of actions and
    #checks to see if the day should be advanced
    def addCount(self, num):
        self.actionCount += num
        if self.actionCount >= self.actions:
            self.actionCount = 0
            gameTime.advanceDay()
            
    #for lvling up, maybe also special foods?
    def addActions(self, num):
        self.actions += num

# A special type of list that stores a player's inventory
# Only store Items here otherwise bad stuff will happen
class Inventory(list):
    def add(self, item):
        self.append(item)

    # def remove(self, item) comes for free :)

    def removeType(self, itemType, quantity=1):
        removedQuantity = 0;
        for item in self:
            if item.name == itemType.name:
                self.remove(item)
                removedQuantity += 1

                if removedQuantity == quantity:
                    break

        if removedQuantity < quantity:
            raise RuntimeError("Not enough %s to remove." % (itemType))

    def containsType(self, itemType, quantity=1):
        foundQuantity = 0;
        for item in self:
            if item.name == itemType.name:
                foundQuantity += 1

                if foundQuantity == quantity:
                    return True
        return False

    def findType(self, itemType):
        for item in self:
            if item.name == itemType.name:
                return item
        return None
    
    def printSellable(self):
        for item in self:
            if Item.sellable(item) == True:
                print (("%s (%s g)") % (str(Item.name(item)), str(Item.sellPrice(item))))
        print ("")

    def printPretty(self):
        for x in self:
            print (("%s") % (str(Item.__str__(x))))



currentPlayer = Player(0, 15, 10, 0)
for i in range(5):
    currentPlayer.inventory.add(Item(bark))
currentPlayer.inventory.add(Item(blueberry, 5)) # top quality blueberry
