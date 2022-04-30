class Card:
    """ This class represents a playing card.
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""
    # these lists are used in __str__
    # they are class variables rather than instance variables and are shared by each object of the class
    __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]
    __suits = ["", "Clubs", "Diamonds", "Hearts", "Spades" ]

    # region constructor

    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    # endregion

    # region getters and setters

    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

    @suit.setter
    def suit(self, suit):
        if isinstance(suit, int) and 1 <= suit <= 4:
            self.__suit = suit
        else:
            raise ValueError(f"Suit must be an integer between 1 and 4.")

    @value.setter
    def value(self, value):
        if isinstance(value, int) and 1 <= value <= 13:
            self.__value = value
        else:
            raise ValueError(f"Value must be an integer between 1 and 13.")

    # endregion

    # region class functions

    def hasMatchingSuit(self, other):
        return self.suit == other.suit

    def hasMatchingValue(self, other):
        return self.value == other.value

    def isAce(self):
        return self.value == 1

    def isFaceCard(self):
        return 11 <= self.suit <= 13

    def isClub(self):
        return self.suit == 1

    def isDiamond(self):
        return self.suit == 2

    def isHeart(self):
        return self.suit == 3

    def isSpade(self):
        return self.suit == 4

    def isBlack(self):
        return self.suit == 1 or self.suit == 4

    def isRed(self):
        return 2 <= self.suit <= 3

    # endregion

    def __str__(self):
        return f'Card: {Card.__values[self.__value]} of {Card.__suits[self.__suit]}'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.__suit == other.suit and self.__value == other.value
        else:
            return False