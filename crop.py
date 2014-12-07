import random

class Plot(object):
    def __init__ (self, soilLvl, crop):
        self.soilLvl = soilLvl
        self.crop = crop

    def __str__ (self):
        return str(self.crop) + " - " + str(self.soilLvl)

class Field(object):
    def __init__(self):
        self.plotList = []
    
        for i in range(1, 7):
            self.plotList.append( Plot(1, None) )

    def addCrop(self, seed):
        cropAdded = False
        for plot in self.plotList:
            if plot.crop == None:
                plot.crop = seed
                cropAdded = True
                break
        if not cropAdded:
            print "No room in this field for your crop!"

    def __str__ (self):
        outStr=""
        for plot in self.plotList:
            outStr += str(plot) + "\n"
        return outStr
        
fieldOne = Field()

