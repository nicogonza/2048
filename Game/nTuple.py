from preconditions import preconditions
import numpy
import random
import math

class Ntuple():

    numValues = 0
    locations = []
    lookUpTable = []

    # initialize nTuple structure
    def __init__(self, numValues, locations, weights):
        self.numValues = numValues
        self.locations = locations
        self.lookUpTable = weights

    @staticmethod
    @preconditions(lambda locations: len(locations) > 0)
    def randomWeightTuple(numValues, locations, minWeight, maxWeight):
        weights = [Ntuple.computeNewWeights(numValues, len(locations))]
        weights = random.uniform(minWeight, maxWeight, len(weights))
        return Ntuple(numValues,locations,weights)

    def valueAtLocation(self, board):
        return self.lookUpTable[self.tileAddress(board)]

    # compute new weight for move
    @staticmethod
    def computeNewWeights(numValues, numFields):
        return (math.pow(numValues, numFields))# + 0.5)

    def tileAddress(self, board):
        address = 0
        for x in self.locations:
            address *= self.numValues
            address += board.getVal(x)
        return address

    #def valueFromAddress(self, address):
    #    val = []*sys.getSizeOf(val)

    def getNumWeights(self):
        return len(self.lookUpTable)

    def getNumVals(self):
        return self.numValues


    # str test function
    def __str__(self):
        return "Ntuple(" + str(self.numValues) + "," + str(self.locations) + "," + str(self.lookUpTable) + ")"

#tests of tuple creation
ntuple = Ntuple(5, [(0,1),(2,1)],[1,1,1])