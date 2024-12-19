from Classes.Building import Building
from Constants.constants import CAPACITY
class Shop(Building):
    name='shop'
    def __init__(self):
        super().__init__()
        self.capacity=CAPACITY[self.name]