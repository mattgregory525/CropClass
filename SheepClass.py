from AnimalClass import *

class Sheep(Animal):

    """A virtual sheep"""

    def __init__(self):
        super().__init__(2,3,4)
        self._type = "Sheep"


    def grow(self,water,food):
        if water >= self._water_need and food >= self._food_need:
            if self._status == "Unborn":
                self._weight += self._growth_rate * 2
            elif self._status == "Infant":
                self._weight += self._growth_rate * 1.5
            elif self._status == "Young" :
                self._weight += self._growth_rate
            elif self._status == "Mature" :
                self._weight += self._growth_rate / 1.5
            elif self._status == "Old" :
                self._weight += self._growth_rate /2

        self._days_growing += 1
        self._weight += 3
        self._update_status()
            

                
def main():
    sheep_animal = Sheep()
    manage_animal(sheep_animal)

   

if __name__ == "__main__":
    main()
