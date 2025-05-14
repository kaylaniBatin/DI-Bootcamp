#Exercise 1
def display_message():
    print("I am learning about functions in Python.")
display_message()

#Exercise 2
def favorite_book(title):
    print('One of my favorite books is {title}.')
    
favorite_book("Alice in Wonderland")

#Exercise 3

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")
describe_city("Reykjavik", "Iceland")
describe_city("Paris")
describe_city("Tokyo", "Japan")

#Exercise 4
import random
def guess_number(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

guess_number(50)


#Exercise 5
def make_shirt(size, text):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt("small", "Code is life")
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{text}'.")
make_shirt()  # large, default text
make_shirt("medium")  # medium, default text
make_shirt("small", "Custom message")  # custom size and message

make_shirt(size="small", text="Hello!")

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(names):
    for name in names:
        print(name)

def make_great(names):
    for i in range(len(names)):
        names[i] = names[i] + " the Great"

make_great(magician_names)
show_magicians(magician_names)

#Exercise 7
import random

def get_random_temp(season=None):
    if season == "winter":
        return round(random.uniform(-10, 10), 1)
    elif season == "spring":
        return round(random.uniform(10, 20), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 20), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def get_season_from_month(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    elif month in [9, 10, 11]:
        return "autumn"
    else:
        return None


main()