import random
import player as player


craft = {
    "twig" : {"branch" : 1},
    "bark" : {"branch" : 1},
    "string" : {"bark" : 3},
    "pebbles" : {"stone" : 1},
    "cloth" : {"string" : 3, "twig" : 1},
    "dirt" : {"pebbles" : 5},
    "brick" : {"rock" : 2},
    "fruit_dish" : {"blueberry" : 3, "apple" : 1} 
    }

# key : craft[key]:craft[i] 

def print_craft_list(craft):
    for key in craft:
        print (key + " can be made with:")
        for i in craft[key]:
            print (str(craft[key][i]) + " " + i)
        print (" ")

#main runs this
def create_query():
    print ("What do you want to craft?")
    item_create = raw_input(">")
    if item_create in craft:
        item_check(item_create)
    else:
        print "Sorry that item doesn't exist."
    return

#checks if item can be crafted, compares to player inv
#runs create
def item_check(item):
    can_make = True
    for i in craft[item]:
        if (i not in player.pc.inv) or (craft[item][i] > player.pc.inv[i]):
            you_have = player.pc.inv[i] if i in player.pc.inv else 0
            print ("You have " + str(you_have)+ " " + \
                   str(i) + " but you need " + str(craft[item][i]) + ".")
            can_make = False
    if can_make == True:
        create(item)

#item = the thing i want to make
#i = the thing needed to make item
#craft[item][i] = how many i is needed to make item
#player.pc.inv[i] = how many i are in inv
        
def create(item):
    for i in craft[item]:
        count = craft[item][i]
        while count > 0:
            player.pc.remove_inv(i)
            count = count - 1
    player.pc.add_inv(item)
    print ("You made " + str(item) + ".")
            
    

#for testing out item_check, so far all is good
##item_check("twig")
##item_check("cloth")
##item_check("string")
