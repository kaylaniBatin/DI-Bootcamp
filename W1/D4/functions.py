# # #functions
# # #syntax

# # # def func_name():
# # #     '''prints a phrase on the console''' #dog strings explains the function
# # #     print('I am a function')

# # # func_name()
# # # print(print.__doc__)

# # #create a function called greetings that prints 'Hello' in your mother tongue
# # def greetings(language, user_name):
# #     if language == "EN":
# #         print(f'Hello{user_name}')
# #     elif language == "RU":
# #         print(f'Priviet {user_name}')
# #     else:
# #         print('Undefined language')
# # greetings('RU', 'Ilia')

# # #Key word arguements   
# # greetings(user_name = 'Ilia', language = 'RU')

# # #Create a function called country_info that receives a country as an argument 
# # # and print the capital of that country. Make the country name arguement default
# # # Baku 

# # def country_info(country_name = Naboo):
# #     if country_name == "France":
# #     print(f'The capital of {country_info} is Paris')
# # elif country_name == 'Italy':
# #     print(f'the capital of {country_name} is Rome')
# #     else:
# #         print('Country not found')
# # country_info('Naboo')


# # def print_names(*args):  #* args is generic and the *is unlimited)
# #     for name in args:
# #         print(f'Hello, {name}')
# # print_names('Kaylani')

# # #Kwargs key word arguments for dictionarys?

# # def user_info(**kwargs):
# #     print(kwargs)

# # user_info(name = "kaylani", age = 37, address = "tel aviv")

# # #create a function called tasks_manager that accepts tasks and 
# # # prints "today I need to do: {task}"

# def tasks_manager(*args):
#     if args:
#         for arg in args:
#             print(f'Today I need to do {task}')
#     else:
#         print('Please pass a task as argument')

# task_manager('to finish Daily Challenge', 'buy groceries', 'call mom')

# def party_planner(*args, **kwargs):
#     if args:
#         print('you need to buy: ')
#         for arg in args:
#             print(arg)
#     else: 
#         print('there is no food to buy ')
    
#     if kwargs:
#         print('Part details: ')
    
#exercise:
# 1call this function and pass the food and the party details
#2 CALL IT ONLY WITH FOOD INFO
#3call it with only the details


def party_planner(*args, **kwargs):
    if args:
        print('You need to buy: ')
        for arg in args:
            print(arg)
    else:
        print('there is no food to buy' )

    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : \n {value}')
    else:
        print('there are no party details')

print(party_planner)
party_planner(['Pizza', 'Soda', 'Cake'], location = 'Backyard', time = '6 PM')