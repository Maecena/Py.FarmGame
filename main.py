import random
import forest
from player import currentPlayer
import items
import craft
from shop import Shop
import clock as clock


def main():
    runMainMenu()

#Meg's menu system in action
def runMainMenu():
    while True:
        options = {
            1: ("Visit the Forest", "forest"),
            2: ("Go to the Field", "field"),
            3: ("Go to the Barn", "barn"),
            4: ("Open a Vendor Stall", "vendor"),
            5: ("Visit the Market", "market"),
            6: ("Go to the Crafting Bench", "craft"),
            7: ("View Stats", "stats"),
            8: ("Quit", "quit")
        }
        nextAction = displayMenuPrompt(options)

        if nextAction == "forest":
            #works fine
            runForestMenu()

        elif nextAction == "field":
            #does nothing
            runFieldMenu()

        elif nextAction == "barn":
            #does nothing
            runBarnMenu()
        
        elif nextAction == "vendor":
            #works
            runVendorMenu()

        elif nextAction == "market":
            #works
            runMarketMenu()

        elif nextAction == "craft":
            #should be working :D
            runCraftMenu()

        elif nextAction == "stats":
            #works fine
            print (("It is %s %s in Year %s.") % clock.gameTime.checkClock())
            print (("Your money is at %s g, you are at level %s with %s experience and your inventory contains: ") % currentPlayer.printStats())
            currentPlayer.inventory.printPretty()
            
            
            
        elif nextAction == "quit":
            #works!
            print ("Goodbye!")
            exit(0)


            
def runForestMenu():
    print("The forest is an excellent spot to find items!")
    while True:
        print("Where do you want to look?")
        print(" ")

        options = {
            1: ("In a wild field", "wild"),
            2: ("Under the Sunny Brook Bridge", "bridge"),
            3: ("By the Forester's Hut", "hut"),
            4: ("Around Pea Bog", "bog"),
            5: ("By the old mine", "mine"),
            6: ("Go back Home", "home")
        }
        nextAction = displayMenuPrompt(options)

        if nextAction == "wild":
            item = forest.wild.search()
            print ("You found a %s!" % item.name)
            currentPlayer.inventory.add(item)
            currentPlayer.addCount(1)
            currentPlayer.expGain(1)

        elif nextAction == "bridge":
            item = forest.bridge.search()
            print ("You found a %s!" % item.name)
            currentPlayer.inventory.add(item)
            currentPlayer.addCount(1)
            currentPlayer.expGain(1)

        elif nextAction == "hut":
            item = forest.hut.search()
            print ("You found a %s!" % item.name)
            currentPlayer.inventory.add(item)
            currentPlayer.addCount(1)
            currentPlayer.expGain(1)

        elif nextAction == "bog":
            item = forest.bog.search()
            print ("You found a %s!" % item.name)
            currentPlayer.inventory.add(item)
            currentPlayer.addCount(1)
            currentPlayer.expGain(1)

        elif nextAction == "mine":
            item = forest.mine.search()
            print ("You found a %s!" % item.name)
            currentPlayer.inventory.add(item)
            currentPlayer.addCount(1)
            currentPlayer.expGain(1)

        elif nextAction == "home":
            print ("You head home.")
            return

#doing last
def runFieldMenu():
    print ("Nothing Yet")

#also doing last
def runBarnMenu():
    print ("Nothing Yet")

def runVendorMenu():
    print("You can open a stall to sell goods here.")
    Shop.sellPrompt(currentPlayer)

def runMarketMenu():
    print ("You can buy many things at the market!")
    Shop.buyPrompt(currentPlayer)

def runCraftMenu():
    print ("You can craft many things here!")
    while True:
        options = {
                1: ("View all recipes", "recipes"),
                2: ("Check inventory", "inventory"),
                3: ("Craft!", "create"),
                4: ("Go back Home", "home")
            }
        nextAction = displayMenuPrompt(options)

        if nextAction == "recipes":
            craft.printRecipes()
            
        elif nextAction == "inventory":
            currentPlayer.inventory.printPretty()
            
        elif nextAction == "create":
            runCraftCreatePrompt()

        elif nextAction == "home":
            print ("You head home")
            return

def runCraftCreatePrompt():
    print ("What do you want to craft?")
    itemToCreate = input(">")
    if itemToCreate in craft.recipes.keys():
        craft.recipes[itemToCreate].craft(currentPlayer.inventory)
    else:
        print ("Sorry that item doesn't exist.")
    return


#Meg's code... makes the numbered menus work
def displayMenuPrompt(options):
    while True:
        for num, item in options.items():
            print (str(num) + " - " + item[0])

        choice = input(">")

        if not choice.isdigit():
            print ("Please pick a number from 1 to %d. \n" % len(options))
            continue

        choice = int(choice)
        if choice > 0 and choice <= len(options):
            (optionDisplayText, optionInternalText) = options[choice]
            print ("You picked option %d - %s\n" % (choice, optionDisplayText))
            return optionInternalText
        else:
            print("Please pick a number from 1 to %d. \n" % len(options))



main()
