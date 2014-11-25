import random
import player as player

##when new items are added need to update:
##items.all_items,
##allGoods(object),
##search.item_gather_lists,

x = 0

class allGoods(object):
    #Star value will alter buy and sell price later
    #edible will affect eating food and cooking later
    def __init__(self, name, sellable, edible, star, buy, sell):
        self.name = name
        self.sellable = sellable
        self.edible = edible
        self.star = star
        self.buy = buy
        self.sell = sell

    def item_name(self):
        print self.name

    def item_buy_query(self):
        print ("Do you want to buy a " + str(self.name) \
               + " for " + str(self.buy) + " silver?")


    #prints list of sellable items and sell price,
    #called by items.sell_query
    def item_sell_query(self, sellables):
        if self.sellable == True:
            print("You can sell these items:")
            print (str(self.name) + " - " + \
                   str(player.pc.inv_quantity(self.name)))
            sellables.append(1)
            return sellables

    def sale(self):
        player.pc.remove_inv(self.name)
        player.pc.balance_up(self.sell)
        print ("You sold the " + str(self.name) + " for " + \
               str(self.sell) + ".")

    def buy(self):
        player.pc.add_inv(self.name)
        player.pc.balance_down(self.buy)
        
##(self, name, sellable, edible, star, buy, sell)        
#raw food  = allGoods("", True, True, x, 4.0, 2.0)
blue_berry = allGoods("blueberry", True, True, x, 2.0, 1.0)
shijemi = allGoods("shijemi", True, True, x, 3.0, 2.0)
apple = allGoods("apple", True, True, x, 4.0, 2.0)

#crafted food = allGoods("", True, True, x, 4.0, 2.0)
fruit_dish = allGoods("fruit_dish", True, True, x, 16.0, 12.0)

#base  = allGoods("", False, False, x, 1.0, 0)
twig = allGoods("twig", False, False, x, 1.0, 0)
branch = allGoods("branch", False, False, x, 3.0, 0)
bark = allGoods("bark", False, False, x, 1.0, 0)
stone = allGoods("stone", False, False, x, 2.0, 0)
pebbles = allGoods("pebbles", False, False, x, 1.0, 0)
dirt = allGoods("dirt", False, False, x, 1.0, 0)

#craft = allGoods("", False, False, x, 5.0, 0)
string = allGoods("string", False, False, x, 5.0, 0)
cloth = allGoods("cloth", True, False, x, 15.0, 11.0)
brick = allGoods("brick", True, False, x, 4.0, 2.0)

#every item
all_items = {
    "blueberry" : blue_berry,
    "twig" : twig,
    "branch" : branch,
    "bark" : bark,
    "stone" : stone,
    "pebbles" : pebbles,
    "string" : string,
    "shijemi" : shijemi,
    "cloth" : cloth,
    "dirt" : dirt,
    "brick" : brick,
    "apple" : apple,
    "fruit_dish" : fruit_dish
    }

#just the buy-able items
buy_items = ["string", "cloth", "fruit_dish"]

##def get_object(thing):
##    if thing in all_items:
##        # boo = all_items[string]
##        return True

def selling():
    item_name = raw_input(">")
    if item_name in all_items:
        if player.pc.check_inv(item_name) == True:
            item_name = all_items[item_name]
            allGoods.sale(item_name)
    else:
        return False
            
def buying():
    item_name = random.choice(buy_items)
    boo = all_items[item_name]
    allGoods.item_buy_query(boo)
    purchase = raw_input(">")
    if purchase == "yes" or purchase == "y":
        allGoods.buy(boo)
    else:
        return False

    
#loops through all items in pc.inv, prints a list of sellable items
#called by main.runVendorMenu

def sell_query(comp):
    sellables = []
    for key in comp:
        if key in all_items:
            boo = all_items[key]
            allGoods.item_sell_query(boo, sellables)
    return sellables
