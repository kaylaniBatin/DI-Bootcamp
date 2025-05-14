# Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

#Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for member, age in family.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"{member.title()} (age {age}): ${price}")
    total_cost += price
print(f"\nTotal cost: ${total_cost}")

#Exercise 3 zara
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2
print(f"Zara's clients include {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]
print("Last international competitor:", brand["international_competitors"][-1])
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))
print("Number of keys in the dictionary:", len(brand))
print("Keys in the dictionary:", list(brand.keys()))

#Exercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
char_to_index = {user: index for index, user in enumerate(users)}
print("Character to Index:", char_to_index)
index_to_char = {index: user for index, user in enumerate(users)}
print("Index to Character:", index_to_char)
sorted_users = sorted(users)
sorted_char_to_index = {user: index for index, user in enumerate(sorted_users)}
print("Alphabetically Sorted Character to Index:", sorted_char_to_index)
