import random
from fightcards import *
from hazards import *
"""
Main Class for Friday, contains functions to deal with the process of the game
-----
TO DO 
-----
5 Abilities need to be implemented(Destroy card, Exchange Card, Phase -1, Double, and Mimic)
Integration with Web App using Flask
Remove functions whose parameters use global variables
Possible debugging work from missed test cases
Then App is done!
"""
destroyedCards = []
agingDeck = []
missionList = []
hazardDiscards = []
fightDeckDiscards = []
lifePoints = 20
# Functions


#Functions that display stats of unique cards
def displayFightCard(card):
    print("Name: ", card.name, "Score: ", card.fightScore, "Ability: ", card.ability, "| Tapped: ", card.isTapped())


def displayHazard(card):
    print("Hazard: ", card.name, "gives you: ", card.reward, "Score to defeat: ", card.greenScore, "Available draws: ",
          card.drawCount)


def displayMissionList(missionList):
    for x in missionList:
        print(displayFightCard(x))


# calculates remaining draw count given a hazard cards and mission list cards fight cards
def calculateDrawCount(hazardCard):
    global missionList
    total = hazardCard.drawCount
    total = total - len(missionList) - 1
    return total


#Asks user which cards they want to destroy
def clearMissionList(life):
    global missionList, fightDeckDiscards
    counter = life
    while counter > 1:
        displayMissionList(missionList)
        choice2 = int(input("Enter number of card you want to destroy or press 0 to not destroy"))
        #Fixed bug for misNamed Variable here
        if choice2 == -1:
            break;
        elif choice2 == 0:
            counter = counter - 1
        elif choice2 >= 1 or choice2 < len(missionList):
            missionList.pop(choice2 - 1)
            counter = counter - 1
        else:
            print("Please enter a valid number")
    for i in missionList:
        discardPile.append(i)
    missionList.clear()


# Difficulty - fight score of all mission cards given a negative
def calculateLife(hazardCard):
    global missionList
    totalDamage = 0
    if hazardCard.alertLevel == 0:
        totalDamage = int(hazardCard.greenScore)
    elif hazardCard.alertLevel == 1:
        totalDamage = int(hazardCard.yellowScore)
    elif hazardCard.alertLevel == 2:
        totalDamage = int(hazardCard.redScore)
    for x in missionList:
        totalDamage = totalDamage - int(x.fightScore)
    return totalDamage


# Converts Hazard Card and adds into the discards pile
def convertHazardCard(hazardCard):
    global fightDeckDiscards
    fightDeckDiscards.append(hazardCard.convertToReward())


# Checks if deck is empty
def isDeckEmpty(deck):
    if len(deck) == 0:
        return True
    else:
        return False


# UNTESTED METHODS
# If Fight deck empty, set equal to discards and shuffle
def refillFight(discards):
    global ageDeck
    deck = list(discards)
    deck.append(drawFightCard(ageDeck))
    shuffle(deck)
    return deck


def refillHazards(discards):
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
    if lifePoints <= 0:
        print("You have died")
        return True
    else:
        return False


#Handles main game process
def startMission(hazardCard):
    global fightDeck, fightDeckDiscards, missionList
    # if Available draws is negative, subtract from life calc
    availableDraws = 0
    damageNeeded = 0

    while True:
        #Start must check if they lost
        if hasLost():
            break
        choice = int(input("1.)Draw a card  2.) Concede Battle  3.)Use Ability "))
        availableDraws = calculateDrawCount(hazardCard)
        #Checks if decks are out of cards
        if len(fightDeck) < 2:
            fightDeck = refillFight(fightDeckDiscards)
        #Draws card and updates fighting stats
        if choice == 1:
            print("---------------DEBUG----------------")
            displayHazard(hazardCard)
            missionList.append(drawFightCard())
            displayMissionList(missionList)
            damageNeeded = calculateLife(hazardCard)
            print("Available Draws: ", availableDraws)
            print("damageNeeded: ", damageNeeded)
            print("-----------------DEBUG---------------")

        elif choice == 2:
            # Removes life for extra draws
            if damageNeeded <= 0:
                if availableDraws < 0:
                    removeLife(abs(availableDraws) - 1)
                # Win Condition gives user a card
                convertHazardCard(hazardCard)
                clearMissionList(damageNeeded)
                missionList.clear()
                break
            #Loss Condition
            else:
                #Totals damage taken
                if availableDraws < 0:
                    damageNeeded = damageNeeded + abs(availableDraws)
                removeLife(damageNeeded)
                clearMissionList(damageNeeded)
                missionList.clear()
                print(lifePoints)
                break
        #Fight option of using an ability
        elif choice == 3:
            useAbility(fightDeck,hazardCard)
            break;
        else:
            print("oops")

#Prompts user to choose a Hazard card to start a fight
def startHazard():
    global hazardsDeck, hazardDiscards, fightDeck, fightDeckDiscards, missionList
    # Refilling Deck doesn't work with end game
    if len(hazardsDeck) == 1:
        drawHazardCard()
        cards = list(refillHazards(hazardDiscards))
    if len(hazardsDeck) == 0:
        cards = list(refillHazards(hazardDiscards))
    displayHazard(hazardsDeck[0])
    displayHazard(hazardsDeck[1])
    choice = int(input("Which Hazard do you want, 1 or 2?"))
    if choice == 1:
        # Start mission using card of choice
        # Stores unused card into hazard discard pile
        startMission(drawHazardCard())
        # Draws other card from deck and puts into discards
        drawHazardCard()
    else:
        drawHazardCard()
        startMission(drawHazardCard())
        # NEEDS FUNCTION TO USE ABILITY CARDS
        # TO DO - FUNCTION RETURNS LIFE, LIFE FUNCTION TAKES AS INPUT TO DECREASE LIFE IF GREATER THAN 0

#Creates the 10 unique Aging cards
def createAgeDeck():
    ageDeck = []
    ageDeck.append(Suicidal())
    ageDeck.append(Stupid())
    return ageDeck


# Shuffles deck of cards
def shuffle(cards):
    random.shuffle(cards)
    return cards


# Draws a card from a deck of cards
# Removes card from deck
def drawHazardCard():
    global hazardsDeck, hazardDiscards
    drawnCard = hazardsDeck[0]
    hazardDiscards.append(drawnCard)
    hazardsDeck.pop(0)
    return drawnCard


def drawFightCard():
    global fightDeck
    drawnCard = fightDeck[0]
    fightDeck.pop(0)
    return drawnCard


# Creates Deck filled with Aging cards that must be drawn
def createAgingDeck():
    pass
    #


# Add card back into it's respective deck
def addCard(deck):
    pass
    #


def unTapMission(missionList):
    for i in missionList:
        i.unTapCard()

# Allows a vision card to reorganize top 3 cards of deck
def useVision():
    global fightDeck
    temp = []
    for i in range(0, 3):
        temp.append(drawFightCard())
        displayFightCard(temp[i])
    choice1 = int(input("Enter the first card you want to see in deck"))
    temp.insert(0, temp.pop(choice1 - 1))
    for i in range(0, 3):
        displayFightCard(temp[i])
    choice2 = int(input("Enter the second card you want to see in deck"))
    temp.insert(1, temp.pop(choice2 - 1))
    for i in range(0, 3):
        displayFightCard(temp[i])
    choice3 = int(input("Enter the third card you want to see in deck"))
    temp.insert(2, temp.pop(choice3 - 1))
    for j in range(0, len(fightDeck)):
        temp.append(drawFightCard())
    for i in range(0, 3):
        displayFightCard(temp[i])
    return temp


# Calls other Ability functions defined based on name of ability
def useAbility(abilityCard, hazardCard):
    global missionList, fightDeck
    choice = int(input("Which card do you want to use"))
    if missionList[choice - 1].isTapped():
        print(missionList[choice-1].ability)
        print("Card already tapped")
    else:
        if missionList[choice - 1].ability == "Vision":
            useVision(fightDeck)
            missionList[choice-1].tapCard()
        elif missionList[choice - 1].ability == "Mimicry":
            pass
        elif missionList[choice - 1].ability == "Phase":
            pass


# print("Friday is a game about understanding chance and probability of cards to optimize your chances of survival")
# print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
ageDeck = createAgeDeck()
hazardsDeck = createHazardsDeck()
fightDeck = createFightCardsDeck()
shuffle(fightDeck)

smallDeck1 = []
smallDeck2 = []
smallDeck2.append(Vision())
smallDeck2.append(Realization())
print(smallDeck2[0].printAbility())
smallDeck1.append(Raft("raft", "Strategy", 0))
testDiscard = list(hazardsDeck)
testDiscard2 = list(fightDeck)

while True:
    print("---------------DISCARD PILE----------------")
    displayMissionList(fightDeckDiscards)
    print("-----------------DISCARD PULE---------------")
    print("-----------OPTIONS-------------")
    print("1 -> Draw 2 Hazards", "          |Cards in player deck: ", len(fightDeck))
    print("2 -> Use Card Ability", "        |Cards in hazard deck: ", len(hazardsDeck))
    print("3 -> Read Card Ability", "       |Cards in discards deck: ", len(fightDeckDiscards))
    print("4 -> Count Remaining Cards","   |LifePoints:", lifePoints)
    print("-----------OPTIONS---------------")

    choice = int(input("What would you like to do?"))
    print(choice)
    if choice == 1:
        if hasLost():
            break
        startHazard()
        #startHazard(smallDeck1, testDiscard, smallDeck2, testDiscard2, missionList)
        if(lifePoints > 22):
            lifePoints = 22
        print("Life Points:", lifePoints)
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 5:
        pass
    else:
        print("Oops, try again")
