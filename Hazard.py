#10 cards
class Aging:
    def __init__(self, name, fightScore):
        self.name = name
        self.diffScore = fightScore
class suicidal(Aging):
    def __init__(self, name, fightScore):
        super().__init__(name,fightScore)

class Hazard:

    #Hazard cards have a name, winScore, and alert level
    #They also have reward names, which give different abilites
    #Can be turned into reward with unique fight values
    def __init__(self, name, diffScore, Reward,alertLevel, drawCount):
        self.name = name
        self.diffScore = diffScore
        self.Reward = Reward
        self.alertLevel = alertLevel
        self.drawCount
    #Checks if defeated, then turns into reward
    def convertToReward(self):
        pass
class Cannibals(Hazard):
    pass
class WildAnimal(Hazard):
    pass
class Pirates(Hazard):
    def __init__(self, name, diffScore, Reward,alertLevel):
        super().__init__(name,diffScore,Reward, alertLevel)