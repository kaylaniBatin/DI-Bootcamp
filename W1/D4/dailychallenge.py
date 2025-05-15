MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 
import re


new_list = MATRIX_STR.strip().split('\n')
big_list = [list(line) for line in new_list]

message = ''
for col in range(len(big_list[0])):
    for row in big_list:
        message += row[col]

def replace_non_alpha_between_letters(text):
    result = []
    i = 0

    while i < len(text):
        if text[i].isalpha():
            result.append(text[i])
            i += 1
        else:
            while i < len(text) and not text[i].isalpha():
                i += 1
            if result and i < len(text) and text[i].isalpha():
                result.append('')

    return ''.join(result)
print(message)