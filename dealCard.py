
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
    # it has 2 inputs aceCount and number so we're accounting for the times
    # we will have two aces 
    newAceCount = aceCount
    if (number == 11):
        newAceCount += 1
    return newAceCount

def checkDeckSize(deck,defaultDeck):
    if (len(deck) == 0):
        return defaultDeck
    else:
        return deck

def dealCards(cardList,defaultDeck):
    #this function would be returning who won or not and the current deck
    deck = cardList
    dealerAceCount = 0
    playerAceCount = 0
    # these are the number of Ace each player has 

    dealerCard1 = convertCard(deck.pop(random.randint(0,len(deck) - 1)))
    dealerAceCount = aceCount(dealerAceCount,dealerCard1)
    deck = checkDeckSize(deck,defaultDeck);

    playerCard1 = convertCard(deck.pop(random.randint(1,len(deck) - 1)))
    playerAceCount = aceCount(playerAceCount,playerCard1)
    deck = checkDeckSize(deck,defaultDeck);

    dealerCard2 = convertCard(deck.pop(random.randint(1,len(deck) - 1)))
    dealerAceCount = aceCount(dealerAceCount,dealerCard2)
    deck = checkDeckSize(deck,defaultDeck);

    playerCard2 = convertCard(deck.pop(random.randint(1,len(deck) - 1)))
    playerAceCount = aceCount(playerAceCount,playerCard2)
    deck = checkDeckSize(deck,defaultDeck);

    dealerSum = dealerCard1 + dealerCard2
    playerSum = playerCard1 + playerCard2

    print("dealer's two cards are ", dealerCard1, "and", dealerCard2)
    print("players's two cards are ", playerCard1, "and", playerCard2)
    print("dealer sum and Ace count is", dealerSum,dealerAceCount)
    print("player sum and Ace count is", playerSum,playerAceCount)
    print(deck)
    
    while (playerSum < 16):
        print("player sum was initially less than 16")
        playerNewCard = convertCard(deck.pop(random.randint(0,len(deck) - 1)))
        playerSum += playerNewCard
        print("player's new card is ", playerNewCard)
        playerAceCount = aceCount(playerAceCount,playerNewCard)
        deck = checkDeckSize(deck,defaultDeck);
        if (playerSum > 21):
            if (playerAceCount > 0):
                print("There is an Ace, Ace will now be counted as 1")
                playerSum -= 10
                playerAceCount -= 1
            else:
                print("player's sum got over 21 so he lost")
                return -1, deck, len(deck)


    while (dealerSum < 17):
        print("dealer sum was initially less than 17 so he has to hit")
        dealerNewCard = convertCard(deck.pop(random.randint(0,len(deck) - 1)))
        dealerSum += dealerNewCard
        print("dealer's new card is ", dealerNewCard)
        dealerAceCount = aceCount(dealerAceCount, dealerNewCard)
        deck = checkDeckSize(deck,defaultDeck);
        if (dealerSum > 21):
            if (dealerAceCount > 0):
                print("There is an Ace, Ace will now be counted as 1")
                dealerSum -= 10
                dealerAceCount -= 1
            else:
                print("dealer's sum got over 21 so he lost")
                return 1, deck,len(deck)




    print("player's sum is " + str(playerSum))
    print("dealer's sum is " + str(dealerSum))

    #if player wins, return 1; f dealer wins return -1, draw return 0

    if (playerSum > dealerSum):
        return 1,deck,len(deck)
    elif (playerSum < dealerSum):
        return -1,deck,len(deck)
    else:
        return 0,deck,len(deck)

print(dealCards(deck,deck))

