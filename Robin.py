import random

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
#When Deck is depleted, fill with discard and add aging card to fight deck

class FightCard:
    def __init__(self, name, fightScore, ability):
        self.name = name
        self.fightScore = fightScore
        self.tapped = 0
        self.ability = ability
    #Returns name and effect of ability
    def getAbility(self):
        pass

    #Tapps the card
    def tapCard(self):
        self.tapped = 1
    #Untaps Card
    def unTapCard(self):
        self.tapped = 0
    def isTapped(self):
        if(self.tapped == 0):
            return False
        return True
    #checks names and details card ability
    def checkAbility(self):
    #Checks cards ability and performs action
        if(self.ability == "food"):
            print("Food: Restores 1 life point")
        if(self.ability == "eating"):
            print("Food: Restores 2 life point")
        elif(self.ability == "realization"):
            print("realization, destroy one card from mission")
        elif(self.ability == "vision"):
            print("vision, Draw 3 cards, sort them, put at top of deck")
        elif(self.ability == "mimicry"):
            print("Copy one cards ability")
        elif(self.ability == "equipment"):
            print("Draw 2 cards")
        elif(self.ability == "weapon"):
            print("No Effect")
        elif(self.ability == "repeat"):
            print("double fight score")
        elif(self.ability == "book"):
            print("???")
        elif(self.ability == "strategy"):
            print("Exchange two cards from mission and deck")
        elif(self.ability == "phase"):
            print("Drop down phase for mission")
        elif(self.ability == "experience"):
            print("Plus one Card")
            print("Two fight Score")
        else:
            print("There seems to be a mistake")
        #if Ability == Copy
            #Double score of highest card in mission[]
#Uses Inheritance to add specific types of cards
#8
#1 eating
class Weak(FightCard):
    def __init__(self, name="weak", fightScore=0, ability="none"):
        super().__init__(name,fightScore, ability)
#5
class Distracted(FightCard):
    def __init__(self,name="distracted", fightScore="-1",ability="none"):
        super().__init__(name, fightScore, ability)
        self.ability = ability
class Stupid(FightCard):
    def __init__(self, name = "very stupid", fightScore = -3, ability = "none"):
        super().__init__(name,fightScore, ability)
        self.ability = ability
#3
class Focused(FightCard):
    def __init__(self,name = "focused", fightScore = 1,ability = "none"):
        super().__init__(name, fightScore, ability)
#1
class Genius(FightCard):
    def __init__(self,name = "genius", fightScore = 2,ability = "none"):
        super().__init__(name, fightScore, ability)
class Eating(FightCard):
    def __init__(self, name="eating", fightScore=0, ability="+2 Life"):
        super().__init__(name, fightScore, ability)

#10 cards
class Aging:
    def __init__(self, name, fightScore, ability):
        self.name = name
        self.diffScore = fightScore
        self.ability = ability
class Suicidal(Aging):
    def __init__(self, name, fightScore):
        super().__init__(name,fightScore)
class Stupid(Aging):
    def __init__(self, name, fightScore = -2):
        super().__init__(name,fightScore)

class Hazard:

    #Hazard cards have a name, winScore, and alert level
    #They also have reward names, which give different abilites
    #Can be turned into reward with unique fight values
    def __init__(self, name, reward, alertLevel,  greenScore, yellowScore, redScore, drawCount):
        self.name = name
        self.greenScore = greenScore
        self.yellowScore = yellowScore
        self.redScore = redScore
        self.reward = reward
        self.alertLevel = alertLevel
        self.drawCount = drawCount
    #Checks if defeated, then turns into reward
    def convertToReward(self):
        #if reward is "strat" make a strat with 1 fight
        if(self.name == "Raft"):
            freshCard = FightCard(self.reward, 0, self.reward)
        elif(self.name == "Explore"):
            if(self.reward == "weapon"):
                freshCard = FightCard("weapon", 2, "none")
            freshCard = FightCard(self.reward, 1, self.reward)
        elif(self.name == "Further Explore"):
            freshCard = FightCard(self.reward, 2, self.reward)
        elif(self.name == "Wild Animal"):
            freshCard = FightCard(self.reward, 3, self.reward)
        elif(self.name == "Cannibals"):
            freshCard = FightCard("weapon", 4, "none")
        else:
            freshCard = "error"
        return freshCard
    #Increases alert level by 1
    def increaseAlert(self):
        self.alertLevel += 1
    def decreaseAlert(self):
        self.alert -= 1
class Cannibals(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=5, yellowScore=9, redScore=14, drawCount=5):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Cannibals"
        self.reward = "Weapon"
        self.alertLevel = alertLevel
class WildAnimal(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=4, yellowScore=7, redScore=11, drawCount=4):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Wild Animal"
        self.reward = reward
        self.alertLevel = alertLevel
class FurtherExplore(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=2, yellowScore=5, redScore=8, drawCount=3):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Further Explore"
        self.reward = reward
        self.alertLevel = alertLevel
class Explore(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=1, yellowScore=3, redScore=6, drawCount=2):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Explore"
        self.reward = reward
        self.alertLevel = alertLevel
class Raft(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore = 0, yellowScore = 1, redScore = 3, drawCount= 1):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Raft"
        self.reward = reward
        self.alertLevel = alertLevel
class Pirates(Hazard):
    def __init__(self, name, diffScore, Reward,alertLevel):
        super().__init__(name,diffScore,Reward, alertLevel)
def displayFightCard(card):
    print("Name: ", card.name, "Score: ", card.fightScore, "Ability: ", card.ability)
def displayHazard(card):
    print("Hazard: ", card.name, "gives you: ", card.reward, "Score to defeat: ", card.greenScore, "Available draws: ",card.drawCount)
def displayMissionList(missionList):
    for x in missionList:
        print(displayFightCard(x))
#UNTESTED METHOD
# Alters Mission List... Mybe Alter deck...Alter Hazard Cards
def useAbility(hazardCard, missionList, fightCardDeck, fightCard):
    if (fightCard.ability == "eating"):
        global lifePoints
        lifePoints += 1
    elif (fightCard.ability == "hungry"):
        global lifePoints
        lifePoints -= 1
    elif fightCard.ability == "strategy":
        pass
    elif fightCard.ability == "vision":
        pass
    elif fightCard.ability == "phase":
        pass

#calculates remaining draw count given a hazard cards and mission list cards fight cards
def calculateDrawCount(hazardCard, missionList):
    total = hazardCard.drawCount
    total = total - len(missionList) -1
    return total
def clearMissionList(missionList, discardPile, life):
    counter = life
    while(counter > 1):
        displayMissionList(missionList)
        choice2 = int(input("Enter number of card you want to destroy or press 0 to not destroy"))
        if(choice == -1):
            break;
        if(choice2 == 0):
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
def refillFight(deck,discards, ageDeck):
    deck = list(discards)
    deck.append(ageDeck[0])
    shuffle(deck)
    return deck
def refillHazzards(deck, discards):
    deck = list(discards)
    for i in deck:
        i.increaseAlert
    shuffle(deck)
def removeLife(damage):
    global lifePoints
    lifePoints -= damage
#If Deck is empty, set equal to discard deck and shuffle
#If deck is fight add aging card to discard pile and shuffle

def startMission(hazardCard, fightDeck, fightDeckDiscards, missionList):
    #if Available draws is negative, subtract from life calc
    availableDraws = 0
    damageNeeded = 0
    while(True):
        choice = int(input("1.)Draw a card  2.) Concede Battle"))
        availableDraws = calculateDrawCount(hazardCard, missionList)
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
            #Loss
            else:
                if (availableDraws < 0):
                    damageNeeded = damageNeeded + abs(availableDraws)
                #Convert Hazard card and add to discards
                removeLife(damageNeeded)
                clearMissionList(missionList, fightDeckDiscards, damageNeeded)
                missionList.clear()
                print(lifePoints)

            break;
        # If they concede, Ask to choose cards to burn from mission cards
        # Subtract from their lifepoints the hazard.fightscore - total_fightscore
        # if Difference Score is negative, they win if they concede
        # Convert Hazard into FightCard
        # Add FightCard into their discard pile
        # Print you won statement
        else:
            print("oops")
    return lifePoints
def startHazard(cards, discards, fightDeck, fightDeckDiscards, missionList):
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
#Creates fightCards with their constructors to be played in the game
#Returns array filled with starting fightCards
def createFightCardsDeck():
    fightDeck = []
    for i in range(0, 8):
        fightDeck.append(Weak())
    for i in range(0,5):
        fightDeck.append(Distracted())
    for i in range(0,3):
        fightDeck.append(Focused())
    fightDeck.append(Genius())
    fightDeck.append(Eating())
    return fightDeck
#Creates Hazards with their constructors to be played in the game
#Returns array filled with Hazards
def createHazardsDeck():
    # Creates 10 different Raft Cards
    raft1 = Raft("Raft", "strategy", 0)
    raft2 = Raft("Raft", "mimicry", 0)
    raft3 = Raft("Raft", "realization", 0)
    raft4 = Raft("Raft", "deception", 0)
    raft5 = Raft("Raft", "equipment", 0)
    # another unknown effect
    raft6 = Raft("Raft", "???", 0)
    raft7 = Raft("Raft", "book", 0)
    raft8 = Raft("Raft", "food", 0)
    raft9 = Raft("Raft", "food", 0)
    raft10 = Raft("Raft", "food", 0)
    raft11 = Raft("Raft", "equipment", 0)
    # Creates 8 different Explore Cards
    explore1 = Explore("Explore", "repeat", 0)
    explore2 = Explore("Explore", "food", 0)
    explore3 = Explore("Explore", "deception", 0)
    explore4 = Explore("Explore", "weapon", 0)
    explore5 = Explore("Explore", "mimicry", 0)
    explore6 = Explore("Explore", "food", 0)
    explore7 = Explore("Explore", "realization", 0)
    explore8 = Explore("Explore", "weapon", 0)

    # Creates 6 different Further Explore Cards
    furtherExplore1 = FurtherExplore("Further Explore", "realization", 0)
    furtherExplore2 = FurtherExplore("Further Explore", "experience", 0)
    furtherExplore3 = FurtherExplore("Further Explore", "food", 0)
    furtherExplore4 = FurtherExplore("Further Explore", "vision", 0)
    furtherExplore5 = FurtherExplore("Further Explore", "repeat", 0)
    furtherExplore6 = FurtherExplore("Further Explore", "strategy", 0)
    # Creates 4 different Animal Cards
    wild1 = WildAnimal("Wild Animal", "vision", 0)
    wild2 = WildAnimal("Wild Animal", "experience", 0)
    wild3 = WildAnimal("Wild Animal", "red", 0)
    # Not sure what this ability is
    wild4 = WildAnimal("Wild Animal", "strategy", 0)
    # Creates 2 Cannibal Cards
    cannibal1 = Cannibals("Cannibals", "Weapon", 0)
    cannibal2 = Cannibals("Cannibals", "Weapon", 0)
    hazardsDeck = [raft1, raft2, raft3, raft4, raft5, raft6, raft7, raft8, raft9, raft10,
                   explore1, explore2, explore3, explore4, explore5, explore6, explore7, explore8,
                   furtherExplore1, furtherExplore2, furtherExplore3, furtherExplore4, furtherExplore5, furtherExplore6,
                   wild1, wild2, wild3, wild4, cannibal1, cannibal2
                   ]
    return hazardsDeck
print("Building Deck...")
#print("Friday is a game about understanding chance and probability of cards to optimize your chances of survival")
#print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
hazardsDeck = createHazardsDeck()
fightDeck = createFightCardsDeck()
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
       startHazard(hazardsDeck, hazardDiscards, fightDeck, fightDeckDiscards, missionList)
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
