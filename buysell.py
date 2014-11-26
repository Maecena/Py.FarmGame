import random
import player as player
import items as items

buy_items = ["string", "cloth", "fruit_dish"]

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

def sale(item, price):
    player.pc.remove_inv(item)
    player.pc.balance_up(price)
    print ("You sold the " + str(item) + " for " + \
           str(price) + ".")

def buy(item, price):
    player.pc.add_inv(item)
    player.pc.balance_down(price)
        

def selling():
    item_name = raw_input(">")
    if item_name in all_items:
        if player.pc.check_inv(item_name) == True:
            item_name = all_items[item_name]
            price = items.allGoods.get_price(item_name)
            sale(item_name, price)
    else:
        return False

#need to fix buy
def buying():
    item_name = random.choice(buy_items)
    boo = all_items[item_name]
    items.allGoods.item_buy_query(boo)
    purchase = raw_input(">")
    if purchase == "yes" or purchase == "y":
        buy(item_name, price)
    else:
        return False

    
#loops through all items in pc.inv, prints a list of sellable items
#called by main.runVendorMenu
#comp = pc.inv
def sell_query(comp):
    sellables = []
    for key in comp:
        if key in all_items:
            boo = all_items[key]
            items.allGoods.item_sell_query(boo, sellables)
    return sellables
