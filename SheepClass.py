from AnimalClass import *

class Sheep(Animal):

    """A virtual sheep"""

    def __init__(self):
        super()._init__(2,3,4,5)
        self._type = "Sheep"

    def grow(self,light,water,food):
        if light >= self._light_need and water >= self._water_need and food >= self:
