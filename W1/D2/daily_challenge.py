# Challenge 1: Multiples of a Number
number = int(input("Enter a number: "))
length = int(input("Enter the length: "))
multiples = []
i = 1
while i <= length:
    multiples.append(number * i)
    i += 1
print(multiples)

# Challenge 2: Remove Consecutive Duplicate Letters
user_word = input("enter a word. ")
result = ""
i = 0
while i < len(user_word):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]
    i += 1
print(result)

