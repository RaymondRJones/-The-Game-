from fightcards import *


class Hazard:
    # Hazard cards have a name, winScore, and alert level
    # They also have reward names, which give different abilites
    # Can be turned into reward with unique fight values
    def __init__(self, name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount):
        self.name = name
        self.greenScore = greenScore
        self.yellowScore = yellowScore
        self.redScore = redScore
        self.reward = reward
        self.alertLevel = alertLevel
        self.drawCount = drawCount

    # Checks if defeated, then turns into reward
    def convertToReward(self):
        # if reward is "strat" make a strat with 1 fight
        if self.name == "Raft":
            freshCard = FightCard(self.reward, 0, self.reward)
        elif self.name == "Explore":
            if self.reward == "weapon":
                freshCard = FightCard("weapon", 2, "none")
            freshCard = FightCard(self.reward, 1, self.reward)
        elif self.name == "Further Explore":
            freshCard = FightCard(self.reward, 2, self.reward)
        elif self.name == "Wild Animal":
            freshCard = FightCard(self.reward, 3, self.reward)
        elif self.name == "Cannibals":
            freshCard = FightCard("weapon", 4, "none")
        else:
            freshCard = "error"
        return freshCard

    # Increases alert level by 1
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
    def __init__(self, name, reward, alertLevel, greenScore=0, yellowScore=1, redScore=3, drawCount=1):
        super().__init__(name, reward, alertLevel, greenScore, yellowScore, redScore, drawCount)
        self.name = "Raft"
        self.reward = reward
        self.alertLevel = alertLevel


class Pirates(Hazard):
    def __init__(self, name, diffScore, Reward, alertLevel):
        super().__init__(name, diffScore, Reward, alertLevel)


# Returns array filled with Hazards
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
