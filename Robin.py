class Robin:
    lifePoints = 20
    destroyedCards = []
    hazardDeck = []
    agingDeck = []
    missionCards = []
    hazardDiscards = []
    fightDeckDiscards = []
    def __init__(self):
        self.lifePoints = 20

#Functions

#Shuffles deck of cards
def shuffle(cards):
    pass
    #d


#Displays reward/ability and its description

def getReward(reward):
    pass

#Places card into pile to be discarded and eventually added back into deck
def discard(card):
    pass

#Draws a card from a deck of cards
def drawCard(cards):
    pass

#removes card from game existence from array
def burnCard(cards):
    pass
    #

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
    #Returns name and effect of ability
    def getAbility(self):
        pass

    #Tapps the card
    def tapCard(self):
        self.tapped = 1
    def unTapCard(self):
        self.tapped = 0
    #checks names and details card ability
    def checkAbility(self):
    #Checks cards ability and performs action
        if(self.ability == "eating"):
            print("Eating: Restores 1 life point")
        elif(self.ability == "realization"):
            print("realization, destroy one card from mission")
        elif(self.ability == "vision"):
            print("vision, Draw 3 cards, sort them, put at top of deck")
        elif(self.ability == "mimicry"):
            print("Copy one cards fight score")
            #1 fight score
        elif(self.ability == "experience"):
            print("Plus one Card")
            print("Two fight Score")
        #books phase
        #5 9 12
        #8 5 2
    def useAbility(self, Robin):
        if (self.ability == "eating"):
            Robin.lifePoints += 1
        elif (self.ability == "hungry"):
            Robin.lifePoints = Robin.lifePoints - 1
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
class suicidal(Aging):
    def __init__(self, name, fightScore):
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
        if(self.name == "raft"):
            freshCard = FightCard(self.reward, 0, self.reward)
        elif(self.name == "explore"):
            if(self.reward == "weapon"):
                freshCard = FightCard("weapon", 2, "none")
            freshCard = FightCard(self.reward, 1, self.reward)
        elif(self.name == "further explore"):
            freshCard = FightCard(self.reward, 2, self.reward)
        elif(self.name == "wild animal"):
            freshCard = FightCard(self.reward, 3, self.reward)
        elif(self.name == "cannibals"):
            freshCard = FightCard("weapon", 4, "none")
        else:
            freshCard = "error"
        return freshCard
    #Increases alert level by 1
    def increaseAlert(self):
        pass
class Cannibals(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=5, yellowScore=9, redScore=14, drawCount=5):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "wild"
        self.reward = "Weapon"
        self.alertLevel = alertLevel
class WildAnimal(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=4, yellowScore=7, redScore=11, drawCount=4):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "wild"
        self.reward = reward
        self.alertLevel = alertLevel
class FurtherExplore(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=2, yellowScore=5, redScore=8, drawCount=3):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "further explore"
        self.reward = reward
        self.alertLevel = alertLevel
class Explore(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore=1, yellowScore=3, redScore=6, drawCount=2):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Raft"
        self.reward = reward
        self.alertLevel = alertLevel
class Raft(Hazard):
    def __init__(self, name, reward, alertLevel, greenScore = 0, yellowScore = 1, redScore = 3, drawCount= 1):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "raft"
        self.reward = reward
        self.alertLevel = alertLevel
class Pirates(Hazard):
    def __init__(self, name, diffScore, Reward,alertLevel):
        super().__init__(name,diffScore,Reward, alertLevel)
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
    raft8 = Raft("Raft", "food", 0)
    raft9 = Raft("Raft", "food", 0)
    raft10 = Raft("Raft", "equipment", 0)
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
    furtherExplore4 = FurtherExplore("Further Explore", "???Happy", 0)
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
#For Loop to Create Starting Robin Deck
fightDeck = createFightCardsDeck()
hazardsDeck = createHazardsDeck()
print(len(fightDeck))
print(len(hazardsDeck))
print(hazardsDeck[1].reward)
weakCard1 = Weak()
hungry1 = FightCard("Hungry", 0, "Hungry")
print(weakCard1.name)
#print(weakCard1.fightScore)
#print(hungry1.fightScore)
print("Friday is a game about understanding chance and probability of cards to optimize your chances of survival")
print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
robin = Robin()
while(True):
    print("1 -> Draw Hazards")
    print("2 -> Use Card Ability")
    print("3 -> Read Card Ability")
    print("4 -> Count Remaining Cards")
    choice = input("What would you like to do?")
    if(choice == 1):
        #DrawCard(Hazards)
        #DrawCard(Hazards)
        #Print Hazard Cards name, effect, drawcount, Reward
        #Ask which card they pick
        #FightStarted = True
        #if they want to draw card, enter 1
        #Ask if they want to concede
        #Calculate lifepoints
        pass
    elif(choice == 2):
        pass
    elif(choice == 3):
        pass
    elif(choice == 4):
        pass
    elif(choice == 5):
        pass
    print("Choose a Hazard for him to face")
    print("Life Points: ",robin.lifePoints)
    break;