#Challenge 1: Sorting

input_string = input("Enter words separated by commas: ")

words_list = input_string.split(',')

words_list.sort()

sorted_string = ','.join(words_list)


print(sorted_string)

#Challenge 2
def longest_word(sentence):
   
    words = sentence.split()

    longest = ""
 
    for word in words:
        if len(word) > len(longest):
            longest = word
    
  
    return longest