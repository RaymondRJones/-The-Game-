class Robin:
    lifePoints = 20
    destroyedCards = []
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


#Displays reward/ability and it's description

def getReward(reward):
    pass
    #f

#Places card into pile to be discarded and eventually added back into deck
def discard(card):
    pass
    #

#Draws a card from a deck of cards
def drawCard(cards):
    pass
    #
#removes card from game existence from array
def burnCard(cards):
    pass
    #

#Creates Hazards with their constructors to be played in the game
#Returns array filled with Hazards
def createHazards():
    pass
    #
#Creates fightCards with their constructors to be played in the game
#Returns array filled with starting fightCards
def createFightCardsDeck():
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
        super().__init__(name, fightScore)
        self.ability = ability
class Stupid(FightCard):
    def __init__(self, name, fightScore, ability):
        super().__init__(name,fightScore)
        self.ability = ability
#3
class Focused(FightCard):
    def __init__(self,name, fightScore,ability):
        super().__init__(name, fightScore, ability)
#1
class Genius(FightCard):
    def __init__(self,name, fightScore,ability):
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
        elif(self.name == "explore"):
            freshCard = FightCard(self.reward, 3, self.reward)
        elif(self.name == "explore"):
            freshCard = FightCard("weapon", 4, "none")
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


raft1 = Raft("jimmy", "strategy", 0)
print(raft1.yellowScore)
weakCard1 = Weak()
hungry1 = FightCard("Hungry", 0, "Hungry")
print(weakCard1.name)
#print(weakCard1.fightScore)
#print(hungry1.fightScore)
print("Friday is a game about understanding chance and probability of cards to optimize your chances of survival")
print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
robin = Robin()
while(True):
    choice = input("What would you like to do?")
    print("1 -> Draw Hazards")
    print("2 -> Use Card Ability")
    print("3 -> Read Card Ability")
    print("4 -> Count Remaining Cards")
    if(choice == 1):
        #DrawCard(Hazards)
        #DrawCard(Hazards
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