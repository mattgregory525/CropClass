from SheepClass import *
from CowClass import *

def display_menu():
    print()
    print("Which animal would you like to create?")
    print()
    print("1. Sheep")
    print("2. Cow")
    print()
    print("Please enter your choice: ")

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if choice in (1,2):
                valid = True
            else:
                print("Please enter a valid option")
            
        except ValueError:
            print("Please enter a valid option")
    return choice

def name(new_animal):
    done = False
    while not done:
        name = input("Name your animal: ")
        if len(name) == 0:
            print("You must enter a name")
        else:
            new_animal._name = name
            done = True

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep()
        new_animal.name = name(new_animal)
    elif choice == 2:
        new_animal = Cow()
        new_animal.name = name(new_animal)

    return new_animal
            
def main():
    new_animal = create_animal()
    manage_animal(new_animal)
    

if __name__ == "__main__":
    main()
