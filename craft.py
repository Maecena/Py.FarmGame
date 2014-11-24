import random

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

def create():
    print ("What do you want to craft?")
    item_create = raw_input(">")
    if item_create in craft:
