import os

#python file I/O - input/output

#old school way of opening a file with python
# file_object = open() #add thee path to the () with r
# print(file_object)

#modern way

#with open(r'C:\Users\kayla\OneDrive\Desktop\DI-Bootcamp\W2\D4\secrets.txt',  encoding='utf-8') as file_obj:
    #READING METHODS
    #output = file_obj.read() #returns the whole content on the file.
    #output = file_obj.readline() #returns one line
    # #returns a list where each line is an element

    #print(output)

#with open(r'C:\Users\kayla\OneDrive\Desktop\DI-Bootcamp\W2\D4\STARWARS.txt', encoding='utf-8') as file_obj:
#bullet 4 -exercise in class
#    list_str = file_obj.readlines()
    
 #   for line in list_str:
 #       print(line.split())

#last bullet point
    # list_str = file_obj.readlines()
    # print(list_str)

    # updated_name = []
    # for line in list_str:
    #     if line =='Luke\n':
    #     updated_name.append('Luke Skywalker')

    # output = ''.join(updated_name)
    # print(output)

    
     

   
    #while True: #way to print line by line
       # line = file_obj.readline()
       # if not line:
        #    break
        #print(line)
    
    #output = file_obj.readline()
    #print(output[6])


#withing on a file   #a ammend(add), #w delete what is there and write somethingnew
#with open(r'C:\Users\kayla\OneDrive\Desktop\DI-Bootcamp\W2\D4\STARWARS.txt', 'a', encoding='utf-8') as file_obj:
    #file_obj.writeline

    #\n add on new line
    #file_obj.writelines('\nHello Python I/O)

#dir_path = os.path.dirname(os.path.realpath(__file__))

#with open(f'{dir_path}/file name, 'a', encoding='utf-8') as file_obj: #searching for the file in a better way


#JSON JavaScript Object Notation (main language inbetween applications)

