# Challenge 1: letter index dictionary

user_word = input("enter a word. ") #dodo
out_dict = {}
for i, char in enumerate(user_word):
    if char in out_dict:
        out_dict[char].append(i)
    else:
        out_dict.update({char : [i] })
print(out_dict)

# Challenge 2:Affordable items

items_purchased = {'Water': '$1',
                   'Bread': '$3',
                   'TV': '$1,000',
                   "Fertilizer": '$20'}
wallet = '$300'
wallet = int(wallet.replace('$', '').replace(',', ''))
basket = []

for items_name, price in items_purchased.items():
    price = price.replace('$', '').replace(',', '')
    price = int(price)
    price = int(price)

    if price < wallet:
        basket.append(items_name)
    else:
        continue
if basket:
    basket = sorted(basket)
    print(basket)
else:
    print('Nothing')

