# anagrams.py

from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Choose an option (1 or 2): ").strip()

        if choice == '2':
            print("Goodbye!")
            break
        elif choice == '1':
            user_input = input("Enter a single word: ").strip()

            # Validate input
            if ' ' in user_input:
                print(" Error: Please enter only one word (no spaces).")
                continue
            if not user_input.isalpha():
                print(" Error: Only alphabetic characters are allowed.")
                continue

            word = user_input.strip()

            # Check if valid word
            if not checker.is_valid_word(word):
                print(f" '{word}' is not a valid English word.")
                continue

            # Get and display anagrams
            anagrams = checker.get_anagrams(word)

            print(f"\nYOUR WORD: \"{word.upper()}\"")
            print("This is a valid English word.")
            if anagrams:
                print("Anagrams for your word:", ', '.join(anagrams))
            else:
                print("No anagrams found.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()
