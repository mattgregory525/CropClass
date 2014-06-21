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

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_animal = Sheep()
    elif choice == 2:
        new_animal = Cow()
    return new_animal
            
def main():
    new_animal = create_animal()
    

if __name__ == "__main__":
    main()
