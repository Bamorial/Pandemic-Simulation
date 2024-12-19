from Classes.Building import Building
class Hospital(Building):
    def __init__(self):
        super().__init__()
        self.capacity=20