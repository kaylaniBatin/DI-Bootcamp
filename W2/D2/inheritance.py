class Parent:
    def speak(self):
        print(f'parent is speaking')

class Child(Parent):
    pass

class Grandchild(Child):
    pass

obj1 = Child()
obj1.speak()

obj2 = Grandchild()
obj2.speak

class Animal:
    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs
        self.fullname = f'{name} {family}'

class Dog(Animal):
    def bark(self): #creating a method
        print(f'A {self.name} is barking')

    def sleep(self):
        return f'{self.name} is sleeping - from the Dog class'


#create a cat class that inherit from animal.
#create a method called get_crazy that prints 
# "a self.name is running with its self.legs legs in full power"



class Cat(Animal):
    def __init__(self, name, family, legs, trained, nick_name):
        super().__init__(name, family, legs)
        self.trained = trained
        self.nickname = nick_name
        

    def get_crazy(self):
        print(f'a {self.name} is running with its {self.legs} legs in full power.')

class Alien:
    def __init__(self, personal_name, planet):
        self.personal_name = personal_name
        self.planet = planet

    def fly(self):
        return f'{self.name} is flying around'
    
    def sleep(self):
        return f'{self.name} is sleeping - from the Alien class'
    
    def make_sound(self):
        return f'{self.name} is making a sound from Alien'
    
class AleinDog(Dog, Alien):
    def __init__(self, name, family, legs, personal_name, planet):
        Dog.__init__(self, name, family, legs)
        Alien.__init__(self, personal_name, planet)




aliendog1 = AleinDog('Dog', 'Canine', 4, 'Astro', 'Mars')

print(aliendog1.name, aliendog1.family, aliendog1.personal_name, aliendog1.planet)
cat_1 = Cat('Cat', 'feline', 4, True, 'cute cute')
cat_1.get_crazy()

print(cat_1.__dict__)


lion = Animal('Lion', 'felidea', 4 ) #object from class animal
print(lion.__dict__)

dog_1= Dog('Dog', 'Canine', 4 )
dog_1.bark()
