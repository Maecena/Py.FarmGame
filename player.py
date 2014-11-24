import random

#items = blueberry , twig , branch , bark , stone , pebbles , string
#shijimi, cloth, dirt

inv = {
    }

class player(object):
    def __init__(self, exp, money, inventory):
        self.exp = exp
        self.money = money
        self.inv = inventory


    def player_stats(self):
        print("Your money is at " + str(self.money) + " silver,")
        print("you have " + str(self.exp) + " experience and")
        print("your inventory contains: ")
        pc.print_inv()

#the money functions add or subtract money
    def balance_down(self, total):
        if self.money >= total:
            self.money = self.money - total
        else:
            print ("Sorry you don't have enough money")
            return False

    def balance_up(self, total):
        self.money = self.money + total

#prints the whole inv key and value
    def print_inv(self):
        for key in self.inv:
            print (str(key) + " - " + str(self.inv[key]))

    def add_inv(self, item):
        if item in self.inv:
            self.inv[item] = self.inv[item] + 1
        else:
            inv[item] = 1

    def remove_inv(self, item):
        if item in self.inv:
            if self.inv[item] > 0:
                self.inv[item] = self.inv[item] - 1
                if self.inv[item] == 0:
                    del self.inv[item]
            else:
                print ("You can't! It's listed but something's broken.")
        else:
            print ("You can't! You don't have any.")

#prints just one value from the inv
    def inv_quantity(self, key):
        if key in self.inv:
            return self.inv[key]

    def check_inv(self, item):
        if item in self.inv:
            return True
        else:
            return False
    
pc = player(0, 15, inv)
