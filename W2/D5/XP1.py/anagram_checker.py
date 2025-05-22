#Mini-project : Anagram checker

# anagram_checker.py

class AnagramChecker:
    def __init__(self, word_list_file='C:\\Users\\kayla\\OneDrive\\Desktop\\DI-Bootcamp\\W2\\D5\\XP1.py\\words.txt'):
        with open(word_list_file, 'r') as file:
            self.word_list = set(word.strip().lower() for word in file.readlines())

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def get_anagrams(self, word):
        word = word.lower()
        anagrams = []
        for w in self.word_list:
            if w != word and self.is_anagram(word, w):
                anagrams.append(w)
        return anagrams

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)


