from Classes.Building import Building

class School(Building):
    def __init__(self):
        super().__init__()
        self.capacity=10