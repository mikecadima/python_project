#my game-virtual pet
class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=50, sadness=50):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.sadness = sadness
        self.toys = []
        self.treats = []

    def eat_food(self):
        self.fullness += 20
        self.hunger -= 5

    def get_love(self):
        self.happiness += 20
        self.sadness -= 5

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

    def get_toy(self):
        self.fullness += 10
        self.happiness += 10
        self.sadness -= 10

    def pizza(self):
        self.fullness += 20
        self.happiness += 20
        self.hunger -= 5
        self.sadness -= 5

    def bacon(self):
        self.fullness += 20
        self.happiness += 20
        self.hunger -= 5
        self.sadness -= 5

    def vegan_snack(self):
        self.fullness += 5
        self.happiness += 5
        self.hunger -= 5
        self.sadness -= 2

    def __str__(self):
        return """
        \033[34m %s: \033[0m
        Fullness: %d
        Happiness: %d
        Hunger: %d
        Sadness: %d
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.sadness)

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, sadness=5):
        super(CuddlyPet,self).__init__(name, fullness,100,hunger,1)
        self.cuddle_level = cuddle_level
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.sadness/2
        for toy in self.toys:
            self.happiness += toy.use()

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

    def __str__(self):
        return "Extra cuddly"



