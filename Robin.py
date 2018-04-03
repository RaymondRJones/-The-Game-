import random
from fightcards import *
from hazards import *

destroyedCards = []
agingDeck = []
missionList = []
hazardDiscards = []
fightDeckDiscards = []
lifePoints = 20
#Functions
"""
block comment
"""


def displayFightCard(card):
    print("Name: ", card.name, "Score: ", card.fightScore, "Ability: ", card.ability)
def displayHazard(card):
    print("Hazard: ", card.name, "gives you: ", card.reward, "Score to defeat: ", card.greenScore, "Available draws: ",card.drawCount)
def displayMissionList(missionList):
    for x in missionList:
        print(displayFightCard(x))
#calculates remaining draw count given a hazard cards and mission list cards fight cards
def calculateDrawCount(hazardCard, missionList):
    total = hazardCard.drawCount
    total = total - len(missionList) -1
    return total
#NEEDS FUNCTION TO DENY DELETION
def clearMissionList(missionList, discardPile, life):
    counter = life
    while(counter > 1):
        displayMissionList(missionList)
        choice2 = int(input("Enter number of card you want to destroy or press 0 to not destroy"))
        if(choice == -1):
            break;
        elif(choice2 == 0):
            counter = counter - 1
        elif(choice2 < 1 or choice2 > len(missionList)):
            print("Please enter a valid number")
        else:
            missionList.pop(choice2 - 1)
            counter = counter - 1
    for i in missionList:
        discardPile.append(i)
    missionList.clear()
#Difficulty - fight score of all mission cards given a negative
def calculateLife(hazardCard, missionList):
    totalDamage = 0
    if(hazardCard.alertLevel == 0):
        totalDamage = int(hazardCard.greenScore)
    elif(hazardCard.alertLevel == 1):
        totalDamage = int(hazardCard.yellowScore)
    elif(hazardCard.alertLevel == 2):
        totalDamage = int(hazardCard.redScore)
    for x in missionList:
        totalDamage = totalDamage - int(x.fightScore)
    return totalDamage
#Converts Hazard Card and adds into the discards pile
def convertHazardCard(hazardCard, fightDeckDiscards):
    fightDeckDiscards.append(hazardCard.convertToReward())
#Checks if deck is empty
def isDeckEmpty(deck):
    if len(deck) == 0:
        return True
    else:
        return False
#UNTESTED METHODS
#If Fight deck empty, set equal to discards and shuffle
def refillFight(deck,discards):
    global ageDeck
    deck = list(discards)
    deck.append(drawFightCard(ageDeck))
    shuffle(deck)
    return deck
def refillHazards(deck, discards):
    deck = list(discards)
    for i in deck:
        i.increaseAlert()
    shuffle(deck)
    discards.clear()
    return deck
def removeLife(damage):
    global lifePoints
    lifePoints -= damage
def hasLost():
    global lifePoints
    if(lifePoints <= 0):
        print("You have died")
        return True
    else: return False
#If Deck is empty, set equal to discard deck and shuffle
#If deck is fight add aging card to discard pile and shuffle

def startMission(hazardCard, fightDeck, fightDeckDiscards, missionList):
    #if Available draws is negative, subtract from life calc
    availableDraws = 0
    damageNeeded = 0
    while(True):
        if(hasLost()):
            break
        choice = int(input("1.)Draw a card  2.) Concede Battle  3.)Use Ability "))
        availableDraws = calculateDrawCount(hazardCard, missionList)
        if(len(fightDeck) < 2):
            print("Length is D: ", len(fightDeckDiscards))
            fightDeck = refillFight(fightDeck, fightDeckDiscards)
        if(choice == 1):
            print("---------------DEBUG----------------")
            displayHazard(hazardCard)
            missionList.append(drawFightCard(fightDeck))
            displayMissionList(missionList)
            damageNeeded = calculateLife(hazardCard, missionList)
            print("Available Draws: ", availableDraws)
            print("damageNeeded: ", damageNeeded)
            print("-----------------DEBUG---------------")
            #Dra
        elif(choice == 2):
            # -> Display MissionList Array
            #Win Condition
            if(damageNeeded <= 0):
                if (availableDraws < 0):
                    removeLife(abs(availableDraws) - 1)
                #life points not working
                convertHazardCard(hazardCard, fightDeckDiscards)
                clearMissionList(missionList, fightDeckDiscards, damageNeeded)
                missionList.clear()
                break
            #Loss
            else:
                if (availableDraws < 0):
                    damageNeeded = damageNeeded + abs(availableDraws)
                #Convert Hazard card and add to discards
                removeLife(damageNeeded)
                clearMissionList(missionList, fightDeckDiscards, damageNeeded)
                missionList.clear()
                print(lifePoints)
                break
        elif(choice == 3):
            #useAbility()
            break;
        # If they concede, Ask to choose cards to burn from mission cards
        # Subtract from their lifepoints the hazard.fightscore - total_fightscore
        # if Difference Score is negative, they win if they concede
        # Convert Hazard into FightCard
        # Add FightCard into their discard pile
        # Print you won statement
        else:
            print("oops")
def startHazard(cards, discards, fightDeck, fightDeckDiscards, missionList):
    #Refilling Deck doesn't work with end game
    if(len(cards) == 1):
        drawHazardCard(cards,discards)
        cards = list(refillHazards(cards, discards))
    if(len(cards) == 0):
        cards = list(refillHazards(cards, discards))
    displayHazard(cards[0])
    displayHazard(cards[1])
    choice = int(input("Which Hazard do you want, 1 or 2?"))
    if (choice == 1):
        #Start mission using card of choice
        #Stores unused card into hazard discard pile
        startMission(drawHazardCard(cards,discards), fightDeck,fightDeckDiscards,missionList)
        #Draws other card from deck and puts into discards
        drawHazardCard(cards,discards)
    else:
        drawHazardCard(cards,discards)
        startMission(drawHazardCard(cards,discards), fightDeck,fightDeckDiscards,missionList)
#NEEDS FUNCTION TO USE ABILITY CARDS
#NEEDS FUNCTION TO ADD AGING CARDS
#NEED TO TEST CONVERT HAZARD TO REWARD
    #TO DO - FUNCTION RETURNS LIFE, LIFE FUNCTION TAKES AS INPUT TO DECREASE LIFE IF GREATER THAN 0
def createAgeDeck():
    ageDeck = []
    ageDeck.append(Suicidal())
    ageDeck.append(Stupid())
    return ageDeck

#Shuffles deck of cards
def shuffle(cards):
    random.shuffle(cards)
    return cards

#Draws a card from a deck of cards
#Removes card from deck
def drawHazardCard(cards, hazardDiscards):
    drawnCard = cards[0]
    hazardDiscards.append(drawnCard)
    cards.pop(0)
    return drawnCard
def drawFightCard(cards):
    drawnCard = cards[0]
    cards.pop(0)
    return drawnCard
#Creates Deck filled with Aging cards that must be drawn
def createAgingDeck():
    pass
    #
#Add card back into it's respective deck
def addCard(deck):
    pass
    #

def unTapMission(missionList):
    for i in missionList:
        i.unTapCard()
#Calls other Ability functions defined based on name of ability
def useAbility(missionList, abilityCard, fightDeck, hazardsDeck):
    choice = int(input("Which card do you want to use"))
    if missionList[choice-1].isTapped :
        print("Card already tapped")
    else:
        if missionList[choice-1].ability == "Vision":
            useVision(fightDeck, abilityCard)
        elif missionList[choice-1].ability == "Mimicry":
            pass
        """"
           changeMimic()
            useAbility()
            tapcard
            changeMimic("mimicry")
        """""


#print("Friday is a game about understanding chance and probability of cards to optimize your chances of survival")
#print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
ageDeck = createAgeDeck()
hazardsDeck = createHazardsDeck()
fightDeck = createFightCardsDeck()
shuffle(fightDeck)

smallDeck1 = []
smallDeck2 = []
smallDeck2.append(Vision())
smallDeck2.append(Realization())
useRealization(smallDeck2, smallDeck2[1])
print(smallDeck2[0].printAbility())
smallDeck1.append(Raft("raft", "Strategy", 0))
testDiscard = list(hazardsDeck)
testDiscard2 = list(fightDeck)

while(True):
    print("---------------DISCARD PILE----------------")
    displayMissionList(fightDeckDiscards)
    print("-----------------DISCARD PULE---------------")
    print("-----------OPTIONS-------------")
    print("1 -> Draw 2 Hazards")
    print("2 -> Use Card Ability")
    print("3 -> Read Card Ability")
    print("4 -> Count Remaining Cards")
    print("-----------OPTIONS---------------")
    print("LifePoints:", lifePoints)

    choice = int(input("What would you like to do?"))
    print(choice)
    if(choice == 1):
        if(hasLost()):
            break
        # startHazard(hazardsDeck, hazardDiscards, fightDeck, fightDeckDiscards, missionList)
        startHazard(smallDeck1, testDiscard, smallDeck2, testDiscard2, missionList)
        print("Life Points:", lifePoints)
    elif(choice == 2):
        pass
    elif(choice == 3):
        pass
    elif(choice == 4):
        print("Cards in player deck: ", len(fightDeck))
        print("Cards in hazard deck: ", len(hazardsDeck))
        print("Cards in discards deck: ", len(fightDeckDiscards))
    elif(choice == 5):
        pass
    else:
        print("Oops, try again")
