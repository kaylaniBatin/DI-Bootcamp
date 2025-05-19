#Exercise 1
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def __init__(self, name, age, eye_color="blue"):
        super().__init__(name, age)
        self.eye_color = eye_color

    def describe(self):
        return f'{self.name} has beautiful {self.eye_color} eyes'

bengal_cat = Bengal("Tiger", 3)
chartreux_cat = Chartreux("Shadow", 5)
siamese_cat = Siamese("Luna", 2)

all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)

sara_pets.walk()

#Exercise 2

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}!"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight against {self.name}!"
        else:
            return f"It's a draw between {self.name} and {other_dog.name}!"


dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 15)
dog3 = Dog("Luna", 4, 25)


print(dog1.bark())            
print(dog2.run_speed())        
print(dog1.fight(dog2))        
print(dog3.fight(dog1))       
print(dog2.fight(dog3))        



#Exercise 4
# Step 1: Create the Person Class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


# Step 2: Create the Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_member = Person(first_name, age)
        new_member.last_name = self.last_name
        self.members.append(new_member)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found in the family.")

    def family_presentation(self):
        print(f"Family {self.last_name}")
        for member in self.members:
            print(f"{member.first_name}, Age: {member.age}")


# Testing the classes

# Create a Family
my_family = Family("Smith")

# Add members to the family
my_family.born("Alice", 17)
my_family.born("Bob", 20)
my_family.born("Charlie", 15)

# Check if members are allowed to go out
my_family.check_majority("Alice")
my_family.check_majority("Bob")
my_family.check_majority("Charlie")

# Display the family presentation
my_family.family_presentation()