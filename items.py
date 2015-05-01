import csv

#making the list to call things from
#stored by item number, called like "print seedsList[number].visName"
seedsList = {}
cropsList = {}

class Items(object):
    def __init__(self, itemNumber, visName, basePrice, description, star, tags):
        self.number = itemNumber
        self.visName = visName
        self.description = description
        self.star = star
        self.tags = tags

class Crops(object):
    def __init__(self, cropNumber, visName, basePrice, description, star, tags):
        self.number = cropNumber
        self.visName = visName
        self.basePrice = basePrice
        self.description = description
        self.star = star
        self.tags = tags


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

    def setCrop(self, crop):
        self.crop = crop
        crop.seed = self


#setting up cropsList
def initializeCrops():
    csv.register_dialect('semi', delimiter=';')
    with open('croplist.csv', 'r') as f:
        reader = csv.reader(f, dialect='semi')
        for row in reader:
            cropsList[row[0]] = Crops(row[0], row[1], row[2], row[3], row[4], row[5])


#setting up seedsList
def initializeSeeds():
    f = open('seedlist.csv')
    csv_f = csv.reader(f)

    for row in csv_f:
        seedsList[row[0]] = Seeds(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        Seeds.setCrop(row[0], row[1])


#def initializeItems():
    
#when the page runs this populates the seed and crop dictionaries from the .csv files
initializeCrops()
initializeSeeds()
