from 21 import *
from createDeck import *

def runSimulation(deckCount,deckNumber):
    return 42
    # returns the winning percentage of the player




def run():
    winPercentage = []
    for i in range (11):
        winPercentage += runSimulation(i-5,100)
    return winPercentage



print(run())