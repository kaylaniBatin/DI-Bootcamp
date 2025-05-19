# Daily challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        output = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            output += f"{animal:<10} : {count}\n"
        output += "\n    E-I-E-I-0!"
        return output

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        plural_animals = []

        for animal in animal_list:
            count = self.animals[animal]
            name = animal + "s" if count > 1 else animal
            plural_animals.append(name)

        if len(plural_animals) > 1:
            animals_str = ", ".join(plural_animals[:-1]) + " and " + plural_animals[-1]
        else:
            animals_str = plural_animals[0]

        return f"{self.name}'s farm has {animals_str}."

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_short_info())