#Exerecise 3
import random
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} says woof!"

# Step 2: Define the PetDog class that inherits from Dog
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        all_dogs = [self.name] + list(args)
        print(f"{', '.join(all_dogs)} all play together!")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} hasn't been trained yet.")

# Step 3: Test the PetDog methods
if __name__ == "__main__":
    dog1 = PetDog("Fido", 2, 10)
    dog2 = PetDog("Buddy", 3, 12)
    dog3 = PetDog("Max", 1, 8)

    dog1.train()
    dog1.play(dog2.name, dog3.name)
    dog1.do_a_trick()
