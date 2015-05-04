import random
import items as items



def main():
    items.itemSetup()
    runMainMenu()

#Meg's menu system ^^
def runMainMenu():
    while True:
        options = {
            1: ("Visit the Forest", "forest"),
            2: ("Go to the Field", "field"),
            3: ("Go to the Barn", "barn"),
            4: ("Open a Stall", "vendor"),
            5: ("Visit the Market", "market"),
            6: ("Go to the Crafting Bench", "craft"),
            7: ("View Stats", "stats"),
            8: ("Quit", "quit")
            }
        nextAction = displayMenuPrompt(options)

        if nextAction == "forest":
            runForestMenu()

        elif nextAction == "field":
            runFieldMenu()

        elif nextAction == "barn":
            runBarnMenu()

        elif nextAction == "vendor":
            runVendorMenu()

        elif nextAction == "market":
            runMarketMenu()

        elif nextAction == "craft":
            runCraftMenu()

        elif nextAction == "stats":
            print "Sorry I don't have any numbers for you yet."
            #print stats + day + actions left

        elif nextAction == "quit":
            print "Goodbye! ^_^"
            exit(0)

def runForestMenu():
    print "Sorry this isn't ready yet! :("
    
def runFieldMenu():
    print "Sorry this isn't ready yet! :("

def runBarnMenu():
    print "Sorry this isn't ready yet! :("

def runVendorMenu():
    print "Sorry this isn't ready yet! :("

def runMarketMenu():
    print "Sorry this isn't ready yet! :("

def runCraftMenu():
    print "Sorry this isn't ready yet! :("


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
