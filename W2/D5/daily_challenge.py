import random

# Exercise 1: Quiz Answers

def oop_quiz_answers():
    answers = {
        "What is a class?":
            "A class is a blueprint for creating objects, encapsulating data and behavior into one structure.",
        "What is an instance?":
            "An instance is a specific object created from a class, with its own unique data.",
        "What is encapsulation?":
            "Encapsulation is the concept of restricting direct access to some of an object's components, usually through accessors/mutators.",
        "What is abstraction?":
            "Abstraction means hiding complex implementation details and showing only the necessary features of an object.",
        "What is inheritance?":
            "Inheritance allows one class to inherit attributes and methods from another class.",
        "What is multiple inheritance?":
            "Multiple inheritance allows a class to inherit from more than one parent class.",
        "What is polymorphism?":
            "Polymorphism allows different classes to be treated as instances of the same class through a shared interface.",
        "What is method resolution order or MRO?":
            "MRO is the order in which Python looks for a method in a hierarchy of classes. It's important for determining which method to execute in case of inheritance."
    }

    print("=== OOP Quiz Answers ===")
    for question, answer in answers.items():
        print(f"{question}\n→ {answer}\n")


# Exercise 2: Card and Deck Classes 

# Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


# Deck class (no file path, as per instructions)
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """Reset and shuffle the deck with 52 cards"""
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def deal(self):
        """Deal a single card from the deck"""
        if self.cards:
            return self.cards.pop()
        else:
            return "No cards left in the deck."


# Example usage
if __name__ == "__main__":
    # Run Quiz
    oop_quiz_answers()

    print("=== Deck Operations ===")
    deck = Deck()
    print("Dealing 5 cards:")
    for _ in range(5):
        print(deck.deal())

    print(f"Cards left in deck: {len(deck.cards)}")
