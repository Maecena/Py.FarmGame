## from Singleton import Singleton
#having lots of problems with singleton class
#can't use functions that should work.. gives attributeErrors saying
#singleton instance has no attribute ____

#going to use a regular class instead

#want to have day as a count of actions
#lvling up would increase action count


class Season:
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4


##@Singleton
class Time(object):
    def __init__(self, actions, count, day, season, year):
        self.actions = actions
        self.count = count
        self.day = day
        self.season = season
        self.year = year

    def checkClock(self):
        print "It is %s %s in Year %s. You have %s actions left." \
              % (str(gameTime.seasonFriendly()), str(self.day), \
                 str(self.year), str(self.actions - self.count))

    #updates the count of actions and
    #checks to see if the day should be advanced
    def addCount(self, num):
        self.count += num
        if self.count >= self.actions:
            gameTime.advanceDay()


    #for lvling up, maybe also special foods?
    def addActions(self, num):
        self.actions += num

    #moves time forward! ^_^
    def advanceDay(self):
        self.count = 0
        if self.day < 30:
            self.day += 1
        elif self.season < Season.WINTER:
            self.day = 1
            self.season += 1
        else:
            self.day = 1
            self.season = 1
            self.year += 1
            
        print ""
        print "It's a new day!"
        gameTime.checkClock()
        
        

    #returns the season to be printed
    def seasonFriendly(self):
        if self.season == Season.SPRING:
            return "Spring"
        elif self.season == Season.SUMMER:
            return "Summer"
        elif self.season == Season.FALL:
            return "Fall"
        elif self.season == Season.WINTER:
            return "Winter"

gameTime = Time(15, 0, 1, Season.SPRING, 1)
