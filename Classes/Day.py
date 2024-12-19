class Day:
    currentDay=0
    currentTime=0
    duration=3
    def Reset(self):
        self.currentTime=0
        self.currentDay+=1
    def Increment(self):
        self.currentTime=self.currentTime+1