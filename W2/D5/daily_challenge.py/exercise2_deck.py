# exercise2_deck.py

import random

# Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


# Deck class
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


if __name__ == "__main__":
    print("=== Deck Operations ===")
    deck = Deck()
    print("Dealing 5 cards:")
    for _ in range(5):
        print(deck.deal())

    print(f"Cards left in deck: {len(deck.cards)}")
