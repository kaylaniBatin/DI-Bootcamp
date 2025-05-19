#Exercise 1 Cats

class Cat:

    def __init__(self, name, age):
        print('creating object')
        self.name = name
        self.age = age

black_cat = Cat('Oliver', '2')
white_cat = Cat('Snow', '5')
orange_cat = Cat('Rat', '8')

def find_oldest_cat(black_cat, white_cat, oragne_cat):
    if black_cat.age >= white_cat.age and black_cat.age >= orange_cat.age:
        return black_cat
    elif white_cat.age >= black_cat.age and white_cat.age >= oragne_cat.age:
        return white_cat
    else:
        return oragne_cat

oldest_cat = find_oldest_cat(black_cat, white_cat, orange_cat)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

# Exercise 2 Dogs

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes wolf!')

    def jump(self):
        jump_height = self.height * 2
        print(f'{self.name} jumps {jump_height} cm high!')

davids_dog = Dog('Rex', 40)
sara_dog = Dog('Teacup', 30)

print(f"David's do is names {davids_dog.name} and is {davids_dog.height} cm tall")
davids_dog.bark()
davids_dog.jump()

print(f"sara's dog is names {sara_dog.name} and is {sara_dog.height} cm tall.")
sara_dog.bark()
sara_dog.jump()

if davids_dog.height > sara_dog.height:
    print(f"\n{davids_dog.name} is taller than {sara_dog.name}.")
elif davids_dog.height < sara_dog.height:
    print(f"\n{sara_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"\n{davids_dog.name} and {sara_dog.name} are the same height.")


# Exercise 3 : Who’s the song producer?

# Step 1: Create the Song Class
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Example usage:
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Call the method to print the lyrics
stairway.sing_me_a_song()

# Step 1: Define the Zoo Class
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Current animals in the zoo:")
        for animal in self.animals:
            print(f"- {animal}")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        self.animals.sort()
        self.groups = {}  # reset previous groups
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.groups:
                self.groups[first_letter] = [animal]
            else:
                self.groups[first_letter].append(animal)

    def get_groups(self):
        if not self.groups:
            self.sort_animals()
        print("Animal groups:")
        for letter, group in self.groups.items():
            print(f"{letter}: {group}")

# Step 2: Create a Zoo instance
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal("Cougar")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Zebra")
ramat_gan_safari.add_animal("Lion")

ramat_gan_safari.get_animals()
print()

ramat_gan_safari.sell_animal("Bear")
print()

ramat_gan_safari.get_animals()
print()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()