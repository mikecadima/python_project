#my game-virtual pet
'''
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
'''
class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
        self.treats = []

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()

    def reward_snack(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness        
        for treat in self.treats:
            self.happiness += treat.snack()

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

    def get_toy(self, toy):
        self.toys.append(toy)

    def get_treat(self, treat):
        self.treats.append(treat)

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        super(CuddlyPet,self).__init__(name, fullness,100,hunger,1)
        self.cuddle_level = cuddle_level
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

    def __str__(self):
        return "Extra cuddly"
