from AnimalClass import *

class Cow(Animal):

    """A virtual sheep"""

    def __init__(self):
        super().__init__(2,3,4,5)
        self._type = "Cow"

    def grow(self,light,water,food):
        if light >= self._light_need and water >= self._water_need and food >= self_food_need:
            if self._status == "Unborn":
                self._growth += self._growth_rate * 2.5
            elif self._status == "Infant":
                self._growth += self._growth_rate * 2
            elif self._status == "Young" :
                self._growth += self._growth_rate * 1.5
            elif self._status == "Mature" :
                self._growth += self._growth_rate 
            elif self._status == "Old" :
                self._growth += self._growth_rate /2

        self._days_growing += 1
        self._update_status()
            

                
def main():
    cow_animal = Cow()
    
    

if __name__ == "__main__":
    main()
