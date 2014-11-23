import random
import search as search
import player as player
import items as items


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
            #todo
            runCraftMenu()

        elif nextAction == "stats":
            #works fine
            player.pc.player_stats()

        elif nextAction == "quit":
            #haven't tried yet
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
            5: ("Go back Home", "home")
        }
        nextAction = displayMenuPrompt(options)

        if nextAction == "wild":
            search.gather.find(search.wild)

        elif nextAction == "bridge":
            search.gather.find(search.bridge)

        elif nextAction == "hut":
            search.gather.find(search.hut)

        elif nextAction == "bog":
            search.gather.find(search.bog)

        elif nextAction == "home":
            print ("You head home")
            return




#doing last
def runFieldMenu():
    print ("Nothing Yet")
#also doing last
def runBarnMenu():
    print ("Nothing Yet")



def runVendorMenu():
    print("You can open a stall to sell goods here.")
    while True:
        sellables = items.sell_query(player.pc.inv)
        if len(sellables) == 0:
            print ("Sorry, you have nothing to sell. Come \
back when you have new items.")
            return False
        items.sellables = []
        print("What do you want to sell?")
        vendor_sell = items.selling()
        if vendor_sell == False:
            return False

            
        
        
def runMarketMenu():
    print ("You can buy many things at the market!")
    while True:
        print ("Let's see what this person is selling!")
        market_buy = items.buying()
        if market_buy == False:
            return False

def runCraftMenu():
    print ("Nothing Yet")







#Meg's code... makes the numbered menus work
def displayMenuPrompt(options):
    while True:
        for num, item in options.items():
            print (str(num) + " - " + item[0])

        choice = raw_input(">")

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

