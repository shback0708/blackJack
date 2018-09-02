import random


def createFullDeck():
    final = []
    for i in range (4):
        final.append("A")
        for j in range (9):
            final.append(j+2)
        final.append("J")
        final.append("Q")
        final.append("K")
    return final

def createPlusDeck(plusNumber):
    plusList = ["A",10,"J","Q","K"]
    final = createFullDeck()
    for i in range (plusNumber):
        final.append(plusList[random.randint(0,4)])
    return final

def createMinusDeck(minusNumber):
    minusList = [2,3,4,5,6]
    final = createFullDeck()
    for i in range (abs(minusNumber)):
        final.append(minusList[random.randint(0,4)])
    return final

def createDeck(deckCount):
    if (deckCount >= 0):
        return createPlusDeck(deckCount)
    else:
        return createMinusDeck(deckCount)

