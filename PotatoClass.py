from CropClass import *

class Potato(Crop):

    """A virtual potato"""

    def __init__(self):
        #call superclass constructor
        super().__init__(1,3,6)
        self._type = "Potato"

    #override grow method
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()



def main():
    potato_crop = Potato()
    

if __name__ == "__main__":
    main()
