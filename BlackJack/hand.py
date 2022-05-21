from card import *
from deck import *

class Hand:
    """This class represents a hand of (playing) cards"""

    def __init__(self):
        """constructor that creates an empty hand of cards"""
        self._cards = []

    @property
    def numCards(self):
        """returns the number of cards in the hand"""
        return len(self._cards)

    @property
    def isEmpty(self):
        """returns true when the hand has no more cards and false otherwise"""
        return len(self._cards) == 0

    def addCard(self, card):
        """adds a card to the hand"""
        if isinstance(card, Card):
            self._cards.append(card)
        else:
            raise ValueError(f"Object provided must be a Card.")

    def discard(self, index):
        """discards a specific card from the hand"""
        if isinstance(index, int) and 0 <= index < self.numCards:
            return self._cards.pop(index)
        else:
            raise ValueError(f"Index provided must be an integer within range.")

    def indexOf(self, card):
        """returns the index of a specific card in the hand,
        or returns -1 if the card is not in the hand"""
        if isinstance(card, Card):
            index = 0
            for c in self._cards:
                if c == card:
                    return index
                index += 1
            return -1
        else:
            raise ValueError(f"Object provided must be a Card.")

    def hasCard(self, card):
        """returns true when a specific card is in the hand"""
        if isinstance(card, Card):
            return self.indexOf(card) > -1
        else:
            raise ValueError(f"Object provided must be a Card.")

    def hasCardWithSuit(self, suit):
        """returns true when a card of a specific suit is in the hand"""
        if isinstance(suit, int) and 1 <= suit <= 4:
            for c in self._cards:
                if c.suit == suit:
                    return True
            return False
        else:
            raise ValueError(f"Suit must be an integer between 1 and 4.")

    def hasCardWithValue(self, value):
        """returns true when a card of a specific value is in the hand"""
        if isinstance(value, int) and 1 <= value <= 13:
            for c in self._cards:
                if c.value == value:
                    return True
            return False
        else:
            raise ValueError(f"Value must be an integer between 1 and 13.")

    def fillHand(self, num, deck):
        """deals the specified number of cards to the hand"""
        if isinstance(num, int) and isinstance(deck, Deck):
            for i in range(num):
                self.addCard(deck.deal())
        else:
            raise ValueError(f"Objects provided must be a Card and a Deck.")

    def __getitem__(self, item):
        """Allows a programmer to [] to peek at a card in the hand"""
        if isinstance(item, int):
            return self._cards[item]
        else:
            raise TypeError(f"Index must an int {type(item)}  {item}")

    def __str__(self):
        """creates a string representation of the cards in the hand"""
        output = f"Hand [\n"
        for c in self._cards:
            output += f"\t{c}\n"
        output += "]"
        return output