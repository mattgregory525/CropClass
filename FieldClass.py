from PotatoClass import *
from WheatClass import *
from CowClass import *
from SheepClass import *
import random

class Field:
    """A virtual field"""

    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops


    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False
    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self, position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops": crop_report, "animals": animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["Light need"] > light:
                light = needs["Light need"]
            if needs["Water need"] > water:
                water = needs["Water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["Food need"]
            if needs["Water need"] > water:
                water = needs["water need"]
        return {"Food":food, "Light":light, "Water":water}

    def grow(self,light,food,water):

        if len(self._crops) > 0:
            for crop in self._crops:
                crop.grow(light,water)
                
        if len(self._animals)>0:
            food_required = 0
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs["Food need"]
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0

            for animal in self._animals:
                needs = animal.needs()
                if food >= needs["Food need"]:
                    food -= needs["Food need"]
                    feed = needs["Food need"]
                    if additional_food > 0:
                        additional_food -= 1
                        feed += 1
                    animal.grow(water,feed)
                    
                    
                
            
        
            
    

def display_crops(crop_list):
    print()
    print("The following crops are in the field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos, crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    print("The following animals are in the field: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos, animal.report()))
        pos += 1


def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range (1,length_list+1):
            valid = True
        else:
            print("Please enter a valid option")
    return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range (1,length_list+1):
            valid = True
        else:
            print("Please enter a valid option")
    return selected - 1


def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)


def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)


def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,10)
        field.grow(light, food, water)

def manual_grow(field):
    valid = False
    while not valid:
        try:
            light = int(input("Light value = : "))
            if 1<= light <= 10:
                valid = True
            else:
                print("Please enter a valid input")
        except ValueError:
                print("Please enter a valid input")
    valid = False
    while not valid:
        try:
            water = int(input("Water value = : "))
            if 1<= water <= 10:
                valid = True
            else:
                print("Please enter a valid input")
        except ValueError:
                print("Please enter a valid input")
    valid = False
    while not valid:
        try:
            food = int(input("Food value = : "))
            if 1<= food <= 100:
                valid = True
            else:
                print("Please enter a valid input")
        except ValueError:
                print("Please enter a valid input")
    field.grow(light,food,water)

    
def display_crop_menu():
    print()
    print("Which crop type would you like to add?")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. Neither, take me back")
    print()
    print("Please select an option")

def display_animal_menu():
    print()
    print("Which animal type would you like to add?")
    print()
    print("1. Cow")
    print("2. Sheep")
    print()
    print("0. Neither, take me back")
    print()
    print("Please select an option")

def display_main_menu():
    print()
    print("1. Plant a crop")
    print("2. Harvest a crop")
    print()
    print("3. Create an animal")
    print("4. Remove an animal")
    print()
    print("5. Grow a field manually")
    print("6. Auto grow a field")
    print()
    print("7. Report field status")
    print()
    print("0. Exit program")
    print()
    print("Please select an option")

def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int(input("My choice: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
    return choice


def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Crop not planted")
            print()
    elif choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print("Crop planted")
            print()
        else:
            print()
            print("Crop not planted")
            print()
            

def add_animal_to_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.add_animal(Cow()):
            print()
            print("Animal added")
            print()
        else:
            print()
            print("Animal not added")
            print()
    elif choice == 2:
        if field.add_animal(Sheep()):
            print()
            print("Animal added")
            print()
        else:
            print()
            print("Animal not added")
            print()


def manage_field(field):
    print("This is a field simulation program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        if option ==1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print(" A {0} has been removed".format(removed_crop))
        elif option == 3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("A {0} has been removed".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field,30)
        elif option == 7:
            print(field.report_contents())
            print()
        elif option == 0:
            exit = True
            print()
    print("Thank you for using this program")
            
            
            
            

                         



def main():
    new_field = Field(5,2)
    manage_field(new_field)

   


    
    
   

    


if __name__ == "__main__":
    main()
