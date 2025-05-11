# Exercise 1 Hello World
print("Hello world\n" * 4, end="")

# Exercise 2 Some math
print(99**3*8)

# What is the output?
#(5 < 3) output False
#(3 == 3) output True
#(3 == "3") output error
#("3" > 3) output error
#("Hello" == "hello") output True

# Exercise 4 Computer brand
computer_brand = "Hp"
print(f"I have a {computer_brand} computer.")

# Exercise 5 your information
name = "kaylani"
age = 37
shoe_size = 40
info = (f"I am {name}, {age} years old and I have a large shoe size of {shoe_size}")
print(info)

# Exercise 6 A and B
a = 6
b = 5
if a > b:
    print("Hello world")

# Exercise 7 odd or ever
number = int(input('choose a number'))
if number % 2 == 0:
    print("the number is even.")
else:
    print("the number is odd.")

# Exercise 8 whats your name?
my_name = "Kaylani"
user_name = input("What's your name? ")
if user_name == my_name:
    print("Awesome we have the same name.")

# Exercise 9 Tall enough to ride a roller coaster
height = int(input("Enter your height in centimeters: "))
if height > 145:
    print("You're tall enough to ride!")
else:
    print("Sorry, you need to grow a bit more to ride.")
