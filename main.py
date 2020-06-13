from pet_game import Pet, CuddlyPet


# Begin with no pets.
pets = []
CuddlyPet = []
print("\033[30;4;42m Hello, Welcome to Virtual Pet! \033[0m")
main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give toys to your pets",
    "Give your pet treats",
    "Quit Game"
]

def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "\033[1m Please choose an option: \033[0m"
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice
adoption_menu = [
    "Pet",
    "Cuddly Pet"
]
treat_menu = [
    "coldpizza",
    "bacon",
    "vegansnack"
]
def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            print("Please choose the type of pet:")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(Pet(pet_name))
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy()
        if choice == 6:
            snack_choice = ("What snack would you like to give your pet? ")
            print("Choose from pizza, bacon or vegan snack: ")
            food_choice = get_user_choice(treat_menu)
            if food_choice == 1:
                pet.pizza()
            elif food_choice == 2:
                pet.bacon()
            elif food_choice == 3:
                pet.vegan_snack()

        if choice == 7:
            print("\033[30;4;42m Thank you for playing! \033[0m")
            exit()
        
main()

