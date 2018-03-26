class Hazard:

    #Hazard cards have a name, winScore, and alert level
    #They also have reward names, which give different abilites
    #Can be turned into reward with unique fight values
    def _init_(self, name, diffScore, Reward,alertLevel):
        self.name = name
        self.diffScore = diffScore
        self.Reward = Reward
        self.alertLevel = alertLevel
    #Checks if defeated, then turns into reward
    def convertToReward(self):
