# Daily challenge: Old MacDonald’s Farm
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