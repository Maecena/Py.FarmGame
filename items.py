import csv
import random
#making the list to call things from
#stored by item number, called like "print seedsList[number].visName"
seedDict = {}
cropDict = {}
itemDict = {}
masterDict = {}    


#The big class, all items are in here
class ItemMaster(object):
    def __init__(self, thing, itemNumber, visName, basePrice, description, tags):
        self.thing = thing
        self.itemNumber = itemNumber
        self.visName = visName
        self.basePrice = basePrice
        self.description = description
        self.tags = tags

    def getNumber(self):
        return self.itemNumber

    def getBaseItem(self):
        return self.thing

    def getVisName(self):
        return self.visName


class Items(object):
    def __init__(self, itemNumber, visName, basePrice, description, star, tags):
        self.number = itemNumber
        self.visName = visName
        self.basePrice = basePrice
        self.description = description
        self.star = star
        self.tags = tags

    def getNumber(self):
        return self.number

    def getVisName(self):
        return self.visName

    def getBasePrice(self):
        return self.basePrice

    def getDescription(self):
        return self.description

    def getStar(self):
        return self.star

    def getTags(self):
        return self.tags

class Crops(object):
    def __init__(self, cropNumber, visName, basePrice, description, star, tags):
        self.number = cropNumber
        self.visName = visName
        self.basePrice = basePrice
        self.description = description
        self.star = star
        self.tags = tags
        self.seed = 0

#Overwrites the 0 to the seed object
    def setSeed(self, seed):
        self.seed = seed

    def getNumber(self):
        return self.number

    def getVisName(self):
        return self.visName

    def getBasePrice(self):
        return self.basePrice

    def getDescription(self):
        return self.description

    def getStar(self):
        return self.star

    def getTags(self):
        return self.tags

    def getSeed(self):
        return self.seed


class Seeds(object):
    def __init__(self, seedNumber, cropNumber, visName, basePrice, description, star, growTime, regrow, production, tags):
        self.number = seedNumber
        self.crop = cropNumber
        self.visName = visName
        self.basePrice = basePrice
        self.description = description
        self.star = star
        self.grow = growTime
        self.regrow = regrow
        self.production = production
        self.tags = tags

#Overwrites the cropNumber to the crop object
    def setCrop(self, crop):
        self.crop = crop
        Crops.setSeed(crop, self)

    def getNumber(self):
        return self.number

    def getVisName(self):
        return self.visName

    def getCrop(self):
        return self.crop

    def getBasePrice(self):
        return self.basePrice

    def getDescription(self):
        return self.description

    def getStar(self):
        return self.star

    def getGrow(self):
        return self.grow

    def getRegrow(self):
        return self.regrow

    def getProduction(self):
        return self.production

    def getTags(self):
        return self.tags

        

#setting up itemDict
def initializeItems():
    csv.register_dialect('semi', delimiter=';')
    with open('itemlist.csv', 'r') as f:
        reader = csv.reader(f, dialect='semi')
        for row in reader:
            itemDict[row[0]] = Items(row[0], row[1], row[2], row[3], row[4], row[5])
            
#setting up cropDict
def initializeCrops():
    csv.register_dialect('semi', delimiter=';')
    with open('croplist.csv', 'r') as f:
        reader = csv.reader(f, dialect='semi')
        for row in reader:
            cropDict[row[0]] = Crops(row[0], row[1], row[2], row[3], row[4], row[5])

#setting up seedDict
def initializeSeeds():
    csv.register_dialect('semi', delimiter=';')
    with open('seedlist.csv', 'r') as f:
        reader = csv.reader(f, dialect='semi')
        for row in reader:
            seedDict[row[0]] = Seeds(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])

#goes through every seed in seedDict and changes the cropNumber in each Seeds object to the matching crop object, and adds seeds to each Crops object
def integrateSeeds():
    for seed in seedDict.values():
        cropDictLookup = Seeds.getCrop(seed)
        cropObject = cropDict[cropDictLookup]
        Seeds.setCrop(seed, cropObject)

#set up the masterDict
def initializeMaster():
    for seed in seedDict.values():
        masterDict[Seeds.getNumber(seed)] = ItemMaster(seed, Seeds.getNumber(seed), Seeds.getVisName(seed), Seeds.getBasePrice(seed), Seeds.getDescription(seed), Seeds.getTags(seed))
    for crop in cropDict.values():
        masterDict[Crops.getNumber(crop)] = ItemMaster(crop, Crops.getNumber(crop), Crops.getVisName(crop), Crops.getBasePrice(crop), Crops.getDescription(crop), Crops.getTags(crop))
    for item in itemDict.values():
        masterDict[Items.getNumber(item)] = ItemMaster(item, Items.getNumber(item), Items.getVisName(item), Items.getBasePrice(item), Items.getDescription(item), Items.getTags(item))

##def testing():
##    for crop in cropDict.values():
##        x = Crops.getSeed(crop)
##        print (str(Seeds.getVisName(x)) + str(Crops.getVisName(crop)))

    
#when the page runs this populates the seed and crop dictionaries from the .csv files
def itemSetup():
    initializeItems()
    initializeCrops()
    initializeSeeds()
    integrateSeeds()
    initializeMaster()
