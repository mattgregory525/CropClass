from CropClass import *

class Wheat(Crop):

    """Virtual wheat"""

    def __init__(self):
        #call superclass constructor
        super().__init__(1,5,5)
        self._type = "Wheat"

    #override grow method
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" :
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" :
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate

        self._days_growing += 1
        self._update_status()



def main():
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())

if __name__ == "__main__":
    main()
