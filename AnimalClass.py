class Animal:
    """A virtual animal"""

    def __init__(self,growth_rate,food_need,water_need):

        self._weight = 0
        self._name = None
        self._food_need = food_need
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._water_need = water_need
        self._status = "Unborn"
        self._type = "Generic"

    def needs(self):
        return {"Water need": self._water_need, "Food need": self._food_need}

    def report(self):
        return {"Name": self._name, "Type": self._type, "Status": self._status, "Growth": self._weight, "Days growing": self._days_growing, "Weight": self._weight}


    def _update_status(self):
        if self._weight > 15:
            self.status = "Old"
        elif self._weight >10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Infant"
        elif self._weight == 0 :
            self._status = "Unborn"

    def grow(self,food,water):
        if water >= self._water_need and food >= self._food_need:
            self._weight += self._growth_rate
            self._weight += 3
        self._days_growing += 1
        self._update_status()

    def name(self):
        self._name = input("Please name your animal: ")


def display_menu():
    print()
    print("1. Grow animal")
    print("2. Report status")
    print("0. Exit program")
    print()
    print("Please enter your option")


def get_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice <= 2 :
                valid = True
            else:
                print("Please enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice

def manage_animal(new_animal):
    print("This is an animal managment program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            grow_animal(new_animal,6,6)
        elif option == 2:
            print(new_animal.report())
           
        elif option == 0 :
            noexit = False
            print()
    print("Thank you for using this program")

def grow_animal(new_animal,water,food):
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
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value (1-10): "))
            if 1<= food <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between(1-10)")
                        
        except ValueError:
            print("Value entered not valid - please enter a value between(1-10)")

    new_animal.grow(water,food)

    
    

def main():
    new_animal = Animal(1,6,6)
    manage_animal(new_animal)


if __name__ == "__main__":
    main()
