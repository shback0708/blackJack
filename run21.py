#The question would be how would player decide to hit or not hit
#currently its set at 16

from dealCard import *
from createDeck import *

def runSimulation(deckCount,numberOfGames):
    final = 0
    defaultDeck = createDeck(deckCount)
    currentDeck = createDeck(deckCount)
    for i in range(numberOfGames): 
        result,currentDeck = dealCards(currentDeck,defaultDeck)

    return ((result + numberOfGames / 2) * 100) / numberOfGames


    # returns the winning percentage of the player




def run():
    winPercentage = []
    for i in range (11):
        winPercentage += runSimulation(i-5,1000)
    return winPercentage



print(run())