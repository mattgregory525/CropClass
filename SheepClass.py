from AnimalClass import *

class Sheep(Animal):

    """A virtual sheep"""

    def __init__(self):
        super().__init__(2,3,4,5)
        self._type = "Sheep"


    def name(self):
        done = False
        while not done:
            name = input("Name your animal: ")
            if len(name) == 0:
                print("You must enter a name")
            else:
                self._name = name
                done = True

    def grow(self,light,water,food):
        if light >= self._light_need and water >= self._water_need and food >= self:
            if self._status == "Infant":
                self._growth += self._growth_rate * 2
            elif self._status == "Young" :
                self._growth += self._growth_rate * 1.5
            elif self._status == "Mature" :
                self._growth += self._growth_rate
            elif self._status == "Young" :
                self._growth += self._growth_rate /2

        self._days_growing += 1
        self._weight += 3
        self._update_status()
            

                
def main():
    sheep_animal = Sheep()

if __name__ == "__main__":
    main()
