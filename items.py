import random

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

        
#is this used anywhere?
    def item_name(self):
        print self.name

#required for new buysell page
    def get_price(self):
        return (self.price)

#should work
    def item_buy_query(self):
        print ("Do you want to buy a " + str(self.name) \
               + " for " + str(self.buy) + " silver?")
        price = self.buy
        return (price)

    #prints list of sellable items and sell price,
    #called by items.sell_query

    #fix this
    def item_sell_query(self, sellables):
        if self.sellable == True:
            print("You can sell these items:")
            print (str(self.name) + " - " + \
                   str(player.pc.inv_quantity(self.name)))
            sellables.append(1)
            return sellables

        
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
