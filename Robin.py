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
    def __init__(self, name, fightScore, ability):
        super().__init__("weak",fightScore, ability)
        self.ability = "none"
        self.type = "weak"
#5
class Distracted(FightCard):
    def __init__(self,name, fightScore,ability):
        super().__init__(name, fightScore)
        self.ability = ability
class Stupid(FightCard):
    def __init__(self, name, fightScore, ability):
        super().__init__(name,fightScore)
        self.ability = ability
#3
class Focused(FightCard):
    def __init__(self,name, fightScore,ability):
        super().__init__(name, fightScore)
        self.ability = ability
#1
class Genius(FightCard):
    def __init__(self,name, fightScore,ability):
        super().__init__(name, fightScore)
        self.ability = ability




weakCard1 = Weak("Weak", 0, "None")
hungry1 = FightCard("Hungry", 0, "Hungry")
#print(weakCard1.fightScore)
#print(hungry1.fightScore)

print("Robinson Crusoe has been stranded on an island for weeks, help guide him against the trecherous hazards")
robin = Robin()
while(True):
    choice = input("What would you like to do?")
    print("1 -> Draw Hazards")
    print("2 -> Use Card Ability")
    print("3 -> Read Card Ability")
    print("4 -> Count Remaining Cards")
    if(choice == 1):
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