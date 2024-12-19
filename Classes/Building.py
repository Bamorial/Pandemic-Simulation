import random
from Classes.constants import INFECTION_DURATION, START_RATE, STOP_RATE
class Building:
    name='default'
    def __init__(self):
        self.currentCapacity=0
        self.visitors=[]
    def __repr__(self):
        return "Building " + ' visitors: '+ str(len(self.visitors))

    def newVisit(self,individual):
        self.visitors.append(individual)
        self.currentCapacity+=1
    def InfectRand(self):
        infectionRate=random.randrange(START_RATE, STOP_RATE)
        for i in range(infectionRate):
            index=random.randrange(0,len(self.visitors))
            if self.visitors[index].isHealthy==0 and self.visitors[index].isImmune==False:
                self.visitors[index].isHealthy=INFECTION_DURATION