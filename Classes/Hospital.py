from Classes.Building import Building
from Classes.constants import CAPACITY
class Hospital(Building):
    name='hospital'
    def __init__(self):
        super().__init__()
        self.capacity=50
        self.capacity=CAPACITY[self.name]