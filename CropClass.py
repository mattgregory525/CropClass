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
        return{"Light need": self._light_need,"Water need": self._water_need}


    def report(self):
        #Returns a disctionary containing type, status, days growing
        return {"Type": self._type, "Status": self._status, "Growth": self._growth, "Days growing": self._days_growing}
        

    #Underscores make a class private, meaning they must be accsessed through another method
    def _update_status(self):

        
        if 15 <= self._growth:
            self._status = "Old"
        elif 10 <= self._growth:
            self._status = "Mature"
        elif 5 <= self._growth:
            self._status = "Young"
        elif 0 < self._growth:
            self._status = "Seedling"
        elif self._growth == 0 :
            self._status = "Seed"
       
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
        
def diplay_menu():
    print("1. Grow manually")
    print("2. Grow automatically")
    print("3. Report status")
    print("0. Exit program")
    print("")
    print("Please select a option")


def get_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 4 :
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_crop(crop):
    print("This is a crop managment program")
    print()
    noexit = True
    while noexit:
        diplay_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_grow(crop)
            print()
        elif option == 2:
            auto_grow(crop,30)
            print()
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0 :
            noexit = False
            print()
    print("Thank you for using this program")
        
        
            
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
    manage_crop(new_crop)
    


if __name__ == "__main__":
    main()
    
