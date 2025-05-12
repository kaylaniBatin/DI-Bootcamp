#Lists - a sequence of elements
#syntax (how to create)
#some_list = list("item 1") #empty list (not common onoly to convert other sequence in a list)
#other_list = ["item 2"] # best way to create an empty list

#print(len(some_list))

#assessing by index
#print(some_list[1])

#methonds for lists

#create an empty list called names and add 4 names of your favorite characters of a show


numbers = [5, 10, 15, 20, 25, 50, 20]
if 20 in numbers:
    index = numbers.index(20)
    numbers[index] = 200
print(numbers)

