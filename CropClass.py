import random
class Crop:
    #Doc string
    """ A simulation of a generic food crop"""

    #Constructor
    def __init__(self,growth_rate,light_need,water_need):

        #Set attributes
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #Returns a dictionary containing light/water need
        return{"Light need": self._light_need,"Water need": self._water_need,}


    def report(self):
        #Returns a disctionary containing type, status, days growing
        return {"Type": self._type, "Status": self._status, "Growth": self._growth, "Days growing": self._days_growing}
        

    #Underscores make a class private, meaning they must be accsessed through another method
    def _update_status(self):
        if self._growth > 15:
            self.status = "Old"
        elif self._growth >10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0 :
            self._status = "Seed"
        
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1<= light <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between(1-10)")
                        
        except ValueError:
            print("Value entered not valid - please enter a value between(1-10)")

    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1<= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between(1-10)")
                        
        except ValueError:
            print("Value entered not valid - please enter a value between(1-10)")

    crop.grow(light,water)
def main():
    #Instaniate class
    new_crop = Crop(1,4,3)
    print (new_crop.needs())
    print (new_crop.report())
    manual_grow(new_crop)
    print(new_crop.report())
    


if __name__ == "__main__":
    main()
    
