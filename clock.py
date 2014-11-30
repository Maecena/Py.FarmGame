#want to have day as a count of actions
#lvling up would increase action count

from Singleton import Singleton

#I think most of this is going to be very similar to Megs

class Season:
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4




@Singleton
class Time:
    def __init__(self):
        self.actions = 15
        self.count = 15
        self.day = 1
        self.season = Season.SPRING
        self.year = 1

    def check(self):
        print ("It is " + str(seasonFriendly()) + \
               " " + str(self.day) + " in year " + \
               str(self.year) + ". You have " + \
               str(self.count) + " actions left.")

    def seasonFriendly(self):
        if self.season == Season.SPRING:
            return spring
        elif self.season == Season.SUMMER:
            return summer
        elif self.season == Season.FALL:
            return fall
        elif self.season == Season.WINTER:
            return winter

    def advanceDay(self):
        if self.day


