import random
from createDeck import *

deck = createFullDeck()
print(deck)

def popCard(cardList,defaultDeck):
    if (cardList != []):
        card = cardList.pop(random.randint(1,len(cardList)))
    else:
        card = defaultDeck.pop(random.randint(1,len(cardList)))
    return cardList,card

def convertCard(card):
    # Ace will be tricky cause we have to decide whether A should be 
    # interpreted as 11 or 1
    # for now let's make A's default to be 11
    if (card == "A"):
        return 11
    if (card == "J"):
        return 10
    if (card == "Q"):
        return 10
    if (card == "K"):
        return 10
    return card

def aceCount(aceCount,number):
    #this function will be incrementing Ace Count
    newAceCount = aceCount
    if (number == 11):
        newAceCount += 1
    return newAceCount

def dealCards(cardList,defaultDeck):
    deck = cardList
    print("length of the deck is " + str(len(deck)))
    dealerAceCount = 0
    playerAceCount = 0
    # these are the number of Ace each player has 

    dealerCard1 = convertCard(deck.pop(random.randint(1,len(deck))))
    dealerAceCount = aceCount(dealerAceCount,dealerCard1)
    playerCard1 = convertCard(deck.pop(random.randint(1,len(deck))))
    playerAceCount = aceCount(playerAceCount,playerCard1)
    dealerCard2 = convertCard(deck.pop(random.randint(1,len(deck))))
    dealerAceCount = aceCount(dealerAceCount,dealerCard2)
    playerCard2 = convertCard(deck.pop(random.randint(1,len(deck))))
    playerAceCount = aceCount(playerAceCount,playerCard2)

    dealerSum = dealerCard1 + dealerCard2
    playerSum = playerCard1 + playerCard2

    print("length of the deck is " + str(len(deck)))
    print(dealerSum,dealerAceCount)
    print(playerSum,playerAceCount)
    
    # while (playerSum < 16):
    #     newCard = deck.pop(random.randint(1,len(deck)))
    #     if (playerSum > 21):
    #         if (playerHasAce == True):
    #             playerSum -= 10
    #         else:
    #             return -1


    

    

    # print("player's sum is " + str(playerSum))

    # while (dealerSum < 17):
    #     dealerSum += deck.pop(random.randint(1,len(deck)))

    # print("dealer's sum is " + str(dealerSum))

    # if (dealerSum > 21):
    #     return 1

    # if (playerSum > dealerSum):
    #     return 1
    # elif (playerSum < dealerSum):
    #     return -1
    # else:
    #     return 0

def runSimulation(defaultDeck):
    return 42


dealCards(deck,deck)



