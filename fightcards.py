import random
from hazards import *


class FightCard:
    def __init__(self, name, fightScore, ability):
        self.name = name
        self.fightScore = fightScore
        self.tapped = 0
        self.ability = ability

    # Returns name and effect of ability
    def getAbility(self):
        pass

    # Tapps the card
    def tapCard(self):
        self.tapped = 1

    # Untaps Card
    def unTapCard(self):
        self.tapped = 0

    def isTapped(self):
        if self.tapped == 0:
            return False
        return True

    # checks names and details card ability
    # UNTESTED
    def printAbility(self):
        # Checks cards ability and performs action
        if self.ability == "Food":
            print("Food: Restores 1 life point")
        if self.ability == "Eating":
            print("Food: Restores 2 life point")
        elif self.ability == "Realization":
            print("realization, destroy one card from mission")
        elif self.ability == "Vision":
            print("vision, Draw 3 cards, sort them, put at top of deck")
        elif self.ability == "equipment":
            print("Draw 2 cards for free")
        elif self.ability == "repeat":
            print("double fight score of highest card")
        elif self.ability == "book":
            print("Decreases phase")
        elif self.ability == "phase":
            print("Drop down phase for mission")

        elif self.ability == "experience":
            print("Plus one Card")
            print("Two fight Score")
        elif self.ability == "mimicry":
            print("Copy one cards ability")
        elif self.ability == "strategy":
            print("Exchange two cards from mission and deck")
        elif self.ability == "weapon":
            print("No Effect")
        else:
            print("There seems to be a mistake")
            # if Ability == Copy
            # Double score of highest card in mission[]


# Uses Inheritance to add specific types of cards
# 8
# 1 eating
class Weak(FightCard):
    def __init__(self, name="weak", fightScore=0, ability="none"):
        super().__init__(name, fightScore, ability)


# 5
class Distracted(FightCard):
    def __init__(self, name="distracted", fightScore="-1", ability="none"):
        super().__init__(name, fightScore, ability)
        self.ability = ability


class Stupid(FightCard):
    def __init__(self, name="very stupid", fightScore=-3, ability="none"):
        super().__init__(name, fightScore, ability)
        self.ability = ability


# 3
class Focused(FightCard):
    def __init__(self, name="focused", fightScore=1, ability="none"):
        super().__init__(name, fightScore, ability)


# 1
class Genius(FightCard):
    def __init__(self, name="genius", fightScore=2, ability="none"):
        super().__init__(name, fightScore, ability)


class Eating(FightCard):
    def __init__(self, name="eating", fightScore=0, ability="eating"):
        super().__init__(name, fightScore, ability)

    def useEat(self):
        if not self.isTapped():
            global lifePoints
            lifePoints += 2
            self.tapCard()
        else:
            print("Card already tapped")


class Weak(FightCard):
    def __init__(self, name="weak", fightScore=0, ability="none"):
        super().__init__(name, fightScore, ability)


class Realization(FightCard):
    def __init__(self, name="Realization", fightScore=0, ability="Realization"):
        super().__init__(name, fightScore, ability)


# Creates fightCards with their constructors to be played in the game
# Returns array filled with starting fightCards
def createFightCardsDeck():
    fightDeck = []
    for i in range(0, 8):
        fightDeck.append(Weak())
    for i in range(0, 5):
        fightDeck.append(Distracted())
    for i in range(0, 3):
        fightDeck.append(Focused())
    fightDeck.append(Genius())
    fightDeck.append(Eating())
    return fightDeck


# Allows a vision card to reorganize top 3 cards of deck
def useVision(fightDeck, fightCard):
    temp = []
    for i in range(0, 3):
        temp.append(drawFightCard(fightDeck))
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
        temp.append(drawFightCard(fightDeck))
    for i in range(0, 3):
        displayFightCard(temp[i])
    fightCard.tapCard()
    return temp


class Vision(FightCard):
    def __init__(self, name="Vision", fightScore=0, ability="Vision"):
        super().__init__(name, fightScore, ability)


# Destroys card during a mission
def useRealization(missionList, fightCard):
    if fightCard.isTapped() == True:
        print("Card already used")
    displayMissionList(missionList)
    choice = int(input("Choose card to delete"))
    fightCard.tapCard()
    missionList.pop(choice - 1)


# Allows card to mimic, AKA, take ability until mission ends
def useMimic(missionList, fightCard):
    if fightCard.isTapped():
        print("Must be a mimic card")
    else:
        displayMissionList(missionList)
        choice = int(input("Which card do you want to mimic"))
        # Use Ability of ML[choice-1]
    fightCard.tapCard()

class Mimicry(FightCard):
    def __init__(self, name="Mimicry", fightScore=0, ability="Copy"):
        super().__init__(name, fightScore, ability)
#Asks user to discard missionList card, then draws another card to replace
#Original ability stays in effect
def exchange(missionList, fightCardDeck):
    pass
#Moves card from missionlist back into fightCard Deck
def moveCard(missionList, fightCardDeck):
    pass
#Gives more available draws to user
def drawCard():
    pass
#doubles value of a given fight card
def doubleFight():
    pass
#Removes doubled value of given fight card
def removeDouble():
    pass
#Calculate fightScore
# 10 cards
# I haven't recorded all 10 of these cards yet
class Suicidal(FightCard):
    def __init__(self, name="Suicidal", fightScore=-2, ability="none"):
        super().__init__(name, fightScore, ability)
        self.age = True


class Stupid(FightCard):
    def __init__(self, name="Stupid", fightScore=-2, ability="none"):
        super().__init__(name, fightScore, ability)
        self.age = True


def displayFightCard(card):
    print("Name: ", card.name, "Score: ", card.fightScore, "Ability: ", card.ability)


def displayHazard(card):
    print("Hazard: ", card.name, "gives you: ", card.reward, "Score to defeat: ", card.greenScore, "Available draws: ",
          card.drawCount)


def displayMissionList(missionList):
    for x in missionList:
        print(displayFightCard(x))
