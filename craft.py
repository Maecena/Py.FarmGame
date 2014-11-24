import random
import player as player

#items = blueberry , twig , branch , bark , stone , pebbles , string
#shijimi, cloth, dirt

craft = {
    "twig" : {"branch" : 1},
    "bark" : {"branch" : 1},
    "string" : {"bark" : 3},
    "pebbles" : {"stone" : 1},
    "cloth" : {"string" : 3},
    "dirt" : {"pebbles" : 5}
    }

# key : craft[key]:craft[i] 

###from items.py
##all_items = {
##    "blueberry" : blue_berry,
##    "twig" : twig,
##    "branch" : branch,
##    "bark" : bark,
##    "stone" : stone,
##    "pebbles" : pebbles,
##    "string" : string,
##    "shijimi" : shijimi,
##    "cloth" : cloth,
##    "dirt" : dirt
##    }

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
    return

#checks if item can be crafted, compares to player inv
#runs create
def item_check(item):
    #the for loop causes a problem when the recipe requires more than 1 item.
    #will need to look at that later
    for i in craft[item]:
        print i
        print craft[item][i]
        if i not in player.pc.inv:
            print ("You don't have any " + str(i))
            return
        print player.pc.inv[i]
        if craft[item][i] <= player.pc.inv[i]:
            print ("You can make a " + str(item) + \
                   " with " + str(craft[item]) + " you have " + \
                   str(player.pc.inv[i]) + ".")
##            create(item)
        else:
            print ("You have " + str(player.pc.inv[i])+ " " + \
                   str(i) + " but you need " + str(craft[item][i]) + ".")
            return

#item = the thing i want to make
#i = the thing needed to make item
#craft[item][i] = how many i is needed to make item
#player.pc.inv[i] = how many i are in inv
        
##def create(item):
##    for i in craft[item]:
##        count = craft[item][i]
##        if count > 0:
            
    

#for testing out item_check, so far all is good
##item_check("twig")
item_check("cloth")
##item_check("string")
