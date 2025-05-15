MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 
import re

# Step 1: Convert the string into a 2D list
matrix_lines = MATRIX_STR.strip().split('\n')
matrix = [list(line) for line in matrix_lines]

# Step 2: Read the matrix column-wise (top to bottom, left to right)
columns = len(matrix[0])
rows = len(matrix)

raw_message = ""
for col in range(columns):
    for row in range(rows):
        raw_message += matrix[row][col]


decoded_message = re.sub(raw_message)


print(decoded_message)