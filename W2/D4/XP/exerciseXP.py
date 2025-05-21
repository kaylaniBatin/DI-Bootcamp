#Exercise 1: Random Sentence Generator

import random

def get_words_from_file(file_path):
    """
    Reads a file and returns a list of words.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_random_sentence(length, file_path=r"C:\Users\kayla\OneDrive\Desktop\DI-Bootcamp\W2\D4\XP\words.txt"):
    """
    Generates a random sentence of a specified length using words from the file.
    """
    words = get_words_from_file(file_path)
    if not words:
        return "No words available to create a sentence."
    
    sentence_words = [random.choice(words) for _ in range(length)]
    sentence = ' '.join(sentence_words).lower()
    return sentence

def main():
    print("🌟 Welcome to the Random Sentence Generator!")
    print("This program creates a random sentence using words from a word list.")
    
    try:
        user_input = input("Enter the desired sentence length (between 2 and 20): ")
        sentence_length = int(user_input)

        if 2 <= sentence_length <= 20:
            sentence = get_random_sentence(sentence_length)
            print(f"\nGenerated sentence:\n{sentence}")
        else:
            print("Error: Please enter a number between 2 and 20.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()


#Exercise 2 

import json

# Step 1: Load the JSON string
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add the “birth_date” key
data["company"]["employee"]["birth_date"] = "1990-05-15"

# Step 4: Save the modified JSON to a file
with open("modified_data.json", "w") as file:
    json.dump(data, file, indent=4)
