#Exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        # For string conversion like str(c1)
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        # For developer representation like repr(c1)
        return self.__str__()

    def __int__(self):
        # Converts to int like int(c1)
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            raise TypeError(f"Unsupported type for in-place addition: {type(other)}")
        return self

#Exercise 2
# exercise_one.py

# Import the function from func.py
from func import add_numbers

# Call the function with two numbers
add_numbers(3, 5)


#Exercise 3

# Step 1: Import the required modules
import string
import random

# Step 2: Create a string of all uppercase and lowercase letters
letters = string.ascii_letters  # Includes 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Step 3: Generate a random string of length 5
random_string = ''

for _ in range(5):
    random_char = random.choice(letters)  # Pick one random letter
    random_string += random_char          # Add it to the final string

# Print the result
print("Random string:", random_string)


#Exercise 4

# Step 1: Import the datetime module
import datetime

# Step 2 & 3: Create a function to get and display the current date
def show_current_date():
    today = datetime.date.today()  # Get today's date
    print("Today's date is:", today)

# Call the function
show_current_date()


#Exercise 5
# Step 1: Import the datetime module
import datetime

# Step 2–5: Create a function to calculate and display time left until January 1st
def time_until_new_year():
    # Step 2: Get current date and time
    now = datetime.datetime.now()

    # Step 3: Create a datetime object for Jan 1st of the next year
    next_year = now.year + 1
    jan_first = datetime.datetime(year=next_year, month=1, day=1)

    # Step 4: Calculate the time difference
    time_left = jan_first - now

    # Step 5: Display the result
    print("Time left until January 1st:", time_left)

# Call the function
time_until_new_year()

#Exercise 6
# Step 1: Import the datetime module
import datetime

# Step 2: Create a function to calculate minutes lived
def minutes_lived(birthdate_str):
    # Convert string to datetime object (expecting format: YYYY-MM-DD)
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")

    # Get the current date and time
    now = datetime.datetime.now()

    # Calculate time difference
    time_difference = now - birthdate

    # Convert time difference to total minutes
    minutes = int(time_difference.total_seconds() / 60)

    # Display result
    print(f"You have lived for approximately {minutes:,} minutes.")

# Step 3: Call the function with a sample birthdate
minutes_lived("2000-01-01")


#Exercise 7
from faker import Faker

# Step 3: Create a Faker instance and an empty list of users
faker = Faker()
users = []

# Step 4: Create a function to add users
def generate_users(n):
    for _ in range(n):
        user = {
            'name': faker.name(),
            'address': faker.address(),
            'language_code': faker.language_code()
        }
        users.append(user)

# Step 5: Call the function and print the users list
generate_users(5)

# Display the list of users
for user in users:
    print(user)
    print("-" * 40)