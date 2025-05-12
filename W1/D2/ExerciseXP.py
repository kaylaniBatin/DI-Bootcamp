# Exercise 1 favorit numbers
my_favorite_numbers = {1, 2, 3, 4}
my_favorite_numbers.add(29)
my_favorite_numbers.add(30)
my_favorite_numbers.remove(30)
friend_fav_numbers = {7, 8, 9}
my_favorite_numbers = friend_fav_numbers.union(my_favorite_numbers)

# Exercise 2 Tuple
my_tuple = (1, 3, 5)
temp_list = list(my_tuple)
temp_list.extend([6, 7, 8])
my_tuple = tuple(temp_list)


# Exercise 3 list manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove('Blueberries')
basket.append("Kiwi")
basket.insert(0, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)

# Exercise 4 floats ?? this one is hard
#Create a list containing the following sequence of mixed floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.

number_list = []
for number in range(8):
    number_list.append(number + 0.5)
print(number_list)

# Exercise 5 for a loop
for i in range(1, 21):
    print(i)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercise 6 while loop
my_name = "Kaylani"
while True:
    user_name = input("enter your name: ")
    if user_name == my_name:
        break


#exercise 7 favorite fruits
favorite_fruits = []
while True:
    fruit = input("Enter a favorite fruit: ")
    break
    favorite_fruits.append(fruit)
chosen_fruit = input("Enter the name of any fruit: ")
if chosen_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exerecise 8 Pizza toppings
toppings = []
while True:
    topping = input("Enter a pizza topping (type 'quit' when finished): ")
    if topping.lower() == 'quit':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")
base_price = 10.00
topping_price = 2.50
total_cost = base_price + (len(toppings) * topping_price)
print("\nYour pizza will have the following toppings:")
for t in toppings:
    print(f"- {t}")
print(f"Total cost: ${total_cost:.2f}")

# exercise 9 Cinemax Tickets
total_cost = 0
while True:
    age_input = input("Enter the age of a family member: ")
    break
age = int(age_input)
if age < 3:
        cost = 0
elif age <= 12:
    cost = 10
else:
    cost = 15
total_cost += cost
print(f"\nTotal ticket cost for the family: ${total_cost}")

# Exercise 10: Sandwich Orders
sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")