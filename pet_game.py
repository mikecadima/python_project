#my game-virtual pet

dog = {
    "name": "Bane",
    "Stomach": 100,
    "Joy": 50,
}

# function to feed pet
def feed_pet(pet):
    pet["Stomach"] += 10

def play_with_pet(pet):
    pet["Joy"] += 10

# Decrease pet levels.    
def hungry_and_lonely(pet):
    pet["Stomach"] -= 5
    pet["Joy"] -= 5

# Input for user to interact with pet
while True:
    print("Welcome to Virtual Pet!")
    print("""
Your pet %s's levels:
Stomach: %d
Joy: %d
""" % (dog["name"], dog["Stomach"], dog["Joy"]))
    
    choice = int(input("""
1. Feed the dog
2. Play with the dog
3. Don't do either one
"""))  
   

    if choice == 1:
        feed_pet(dog)
    elif choice == 2:
        play_with_pet(dog)
    elif choice == 3:
        print("Thank you for playing!")
        exit()

    # loop will run, it will need an input or prompted to end game
    hungry_and_lonely(dog)
