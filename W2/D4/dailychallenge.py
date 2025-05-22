import string
import re

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        count = words.count(word.lower())
        return count if count > 0 else f"'{word}' not found in text."

    def most_common_word(self):
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            word = word.strip(string.punctuation)
            frequency[word] = frequency.get(word, 0) + 1
        most_common = max(frequency, key=frequency.get)
        return most_common

    def unique_words(self):
        words = self.text.lower().split()
        unique = set(word.strip(string.punctuation) for word in words)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)


class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans('', '', string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "is", "are", "was", "were", "in", "on", "at", "to", "for", "and", "or", "but", "of", "with"
        }
        words = self.text.lower().split()
        filtered = [word for word in words if word not in stop_words]
        return ' '.join(filtered)

    def remove_special_characters(self):
        return re.sub(r'[^A-Za-z0-9\s]', '', self.text)


# Example usage
if __name__ == "__main__":
    sample_text = "Hello, world! This is a test. Testing, one, two, three."
    
    # Text Analysis
    text = Text(sample_text)
    print("Word frequency for 'test':", text.word_frequency("test"))
    print("Most common word:", text.most_common_word())
    print("Unique words:", text.unique_words())

    # Text Modification
    mod_text = TextModification(sample_text)
    print("Without punctuation:", mod_text.remove_punctuation())
    print("Without stop words:", mod_text.remove_stop_words())
    print("Without special characters:", mod_text.remove_special_characters())
