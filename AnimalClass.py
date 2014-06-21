class Animal:
    """A virtual animal"""

    def __init__(self,food_need,growth_rate,light_need,water_need):

        self.weight = 50
        self.name = None
        self._food_need = food_need
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Unborn"
        self._type = "Generic"

    def needs(self):
        return {"light need": self._light_need, "Water need": self._water_need, "Food need": self._food_need}

    def report(self):
        return {"Type": self._type, "Status": self._status, "Growth": self._growth, "Days growing": self._days_growing}


    def update_status(self):
        if self._growth > 15:
            self.status = "Old"
        elif self._growth >10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Infant"
        elif self._growth == 0 :
            self._status = "Unborn"

    def grow(self,light,water,food):
        if light >= self._light_need and water >= self._water_need and food >= self._food_need:
            self._growth += growth_rate
        self._days_growing += 1
        self._update_status()

def manage_animal(new_animal):
    print("This is a crop managment program")
    print()
    noexit = True
    while noexit:
        diplay_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            feed_animal()
           
        elif option == 0 :
            noexit = False
            print()
    print("Thank you for using this program")

def feed_animal(new_animal):
    
    





def main():
    new_animal = Animal()
if __name__ == "__main__":
    main()
