import random
from player import currentPlayer
from items import *

class Recipe(object):
    def __init__(self, product, components):
        self.product = product
        self.components = components

    def craft(self, inventory):
        # Check that we can make the item
        for component, quantity in self.components.iteritems():
            if not inventory.containsType(component, quantity):
                print "You need %s %s to make the %s." % (quantity, component, self.product)
                return False

        # We have enough of everything, so remove the components and add the product item.
        for component, quantity in self.components.iteritems():
            inventory.removeType(component, quantity)

        craftedItem = Item(self.product, random.randint(3,5)) # stuff we make is high quality!!!
        inventory.add(craftedItem)
        print "You made a beautiful %s-star %s." % (craftedItem.star, craftedItem)


recipes = {
    "twig": Recipe(twig, {branch: 1}),
    "bark": Recipe(bark, {branch: 1}),
    "string": Recipe(string, {bark: 3}),
    "pebbles": Recipe(pebbles, {stone: 1}),
    "cloth": Recipe(cloth, {string: 1, twig: 1}),
    "dirt": Recipe(dirt, {pebbles: 5}),
    "brick": Recipe(brick, {stone: 2}),
    "fruit_dish": Recipe(fruit_dish, {blueberry: 3, apple: 1}),
}

def printRecipes():
    global recipes
    for recipe in recipes.values():
        print "A %s can be made with:" % (recipe.product)
        for component, quantity in recipe.components.iteritems():
            print "(%s) %s" % (quantity, component.name)
        print ""
