#oop:object orirnted programing 

#what is the object
#what is a class

#how to create a class (first leeting capital like ex Dog)

class Dog:

    def __init__(self, name, color, breed, age):
        print('creating object')
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
    
    #funcition inside of a class is called a method
    def bark(self):
        print(f'{self.name} is barking.')

    def walk(self, meters):
        print(f'{self.name} is walking {meters} meters.')

    def birthday(self):
        self.age += 1
        return self
    
    def rename(self, name):
        self.name = name
        return self

        


#An instance or object in the class dog is created
#shelter_dog = Dog()

# #Creating attributed to the instance 
# shelter_dog.color = 'Black'

# pitbull = Dog()

#Creating the instances of Dog after creating the __ini__() method:
shelter_dog = Dog('Rex', 'black', 'shelter', '5')

#Create two objects(instinces of the class dog)

house_dog = Dog('mushu', 'white', 'poodle', '1')

outdoor_dog = Dog('Oliver', 'brown', 'husky', '15')

outdoor_dog.bark()
shelter_dog.walk(500)


print(shelter_dog.__dict__)

my_dogs = [shelter_dog, house_dog, outdoor_dog]
print(shelter_dog.age)
shelter_dog.birthday()
print(shelter_dog)
for dog in my_dogs:

    print(dog.name)

print(type(house_dog))

shelter_dog.rename('Toto')
print(shelter_dog.name)


#print(help(str))

my_dogs_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]

print(my_dogs_objects)

#create the method walk