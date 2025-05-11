# Daily challenge: build up a string
user_input = "Kaylani b."
if len(user_input) < 10:
    print("String not long en0ough.")
elif len(user_input) > 10:
    print("String too long.")
else:
    print("perfect string")
print("first character:", user_input[0])
print("last character:", user_input[-1])
for i in range(1, len(user_input) + 1):
        print(user_input[:i])