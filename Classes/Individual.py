class Individual:
    def __init__(self,id):
        self.id=id
    isHealthy=0
    isImmune=False
    contacted=[]
    def __repr__(self):
        return "Individual "+str(self.id)+": healthy: "+str(self.isHealthy) +', immune: '+ str(self.isImmune)