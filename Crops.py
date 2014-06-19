from WheatClass import *
from PotatoClass import *


def display_menu():
    print()
    print("Which crop would you like to create?")
    print()
    print("1. Potato")
    print("2. Wheat")
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

def  create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop
            
def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == "__main__":
    main()
