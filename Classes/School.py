from Classes.Building import Building
from Classes.constants import CAPACITY
class School(Building):
    name='school'
    def __init__(self):
        super().__init__()
        self.capacity=CAPACITY[self.name]