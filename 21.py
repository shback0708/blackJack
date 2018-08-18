import random

def createFullDeck():
    final = []
    for i in range (10):
        for j in range (4):
            final.append(i+1)
    for k in range (12):
        final.append(10)
    return final

def createPlusTen():
    #Added 10 more 10s for the true deck count of plus 10 
    final = []
    for i in range (10):
        for j in range (4):
            final.append(i+1)
    for k in range (22):
        final.append(10)
    return final

fullDeck = createFullDeck()

def dealCards(cardList):
    deck = cardList
    dealerCard1 = deck.pop(random.randint(1,len(deck)))
    playerCard1 = deck.pop(random.randint(1,len(deck)))
    dealerCard2 = deck.pop(random.randint(1,len(deck)))
    playerCard2 = deck.pop(random.randint(1,len(deck)))

    dealerSum = dealerCard1 + dealerCard2
    playerSum = playerCard1 + playerCard2
    if (dealerCard1 == 1 or dealerCard2 == 1):
        dealerSum += 10
    if (playerCard1 == 1 or playerCard2 == 1):
        playerSum += 10

    while (playerSum < 16):
        playerSum += deck.pop(random.randint(1,len(deck)))

    print("player's sum is " + str(playerSum))

    if (playerSum > 21):
        return -1

    while (dealerSum < 17):
        dealerSum += deck.pop(random.randint(1,len(deck)))

    print("dealer's sum is " + str(dealerSum))

    if (dealerSum > 21):
        return 1

    if (playerSum > dealerSum):
        return 1
    elif (playerSum < dealerSum):
        return -1
    else:
        return 0







print(dealCards(fullDeck))







