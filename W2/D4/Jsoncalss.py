import json
dir_path


#converting a dict to json

my_family = {    #dictionary
    'parents': ['Beth', 'Jerry'],
    'children': ['Summer', 'Morty']
}

with open(f'{dir_path}/family.json', 'w') as f:
    json.dump(my_family, f) #creates new file dump

json_my_family = json.dumps(my_family)
print(json_my_family)  #prints string but is Json

with open(f'{dir_path}/family.json', 'r') as f:
    my_family_2 = json.load(f) #prints a dictionary