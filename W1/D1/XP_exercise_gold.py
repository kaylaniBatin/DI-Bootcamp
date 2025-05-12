# Exercise 1 Hello world I love python
print(('Hello world\n' * 4 + 'I love python\n' * 4).strip())

# Exercise 2 what is the weather
user_month = int(input('enter a month number (1-12): '))
if user_month in [3, 4, 5]:
    print("Season: Spring")
elif user_month in [6, 7, 8]:
    print("Season: Summer")
elif user_month in [9, 10, 11]:
    print("Season: Autumn")
elif user_month in [12, 1, 2]:
    print("Season: Winter")