import random
from collections import defaultdict

from items import *
from clock import gameTime


class Player(object):
    def __init__(self, exp, money):
        self.exp = exp
        self.lvl = 1
        self.money = money
        self.inventory = Inventory()

    def printStats(self):
        print("Your money is at " + str(self.money) + " g, ")
        print("you are at level " + str(self.lvl) + \
              " with " + str(self.exp) + " experience and ")
        print("your inventory contains: ")
        self.inventory.printPretty()

    def expGain(self, num=1):
        self.exp += num
        lvlup = 100 * ((int(self.lvl) * 0.1)+ 1 - 0.1)
        if self.exp >= lvlup:
            gameTime.addActions(1)
            self.lvl += 1
            self.exp = 0
        

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
            if item.sellable == True:
                print ("%s (%s g)" % (str(item), str(item.sellPrice)))

        print ""

    def printPretty(self):
        itemDict = defaultdict(int)
        for item in self:
            itemDict[item.name] += 1

        for name, quantity in itemDict.iteritems():
            print "%s (%s)" % (name, quantity)
        print ""



currentPlayer = Player(0, 15)
for i in range(5):
    currentPlayer.inventory.add(Item(bark))
currentPlayer.inventory.add(Item(blueberry, 5)) # top quality blueberry
