class Card:
    """ This class representa a playing card.  
        A card has 2 attributes, value and suit.  value is an int between 1 and 13.  suit is an int between 1 and 4.
        It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""
    # these lists are used in __str__
    # they are class variables rather than instance variables and are shared by each object of the class
    __values = ["", "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Ten", "Jack", "Queen", "King"]
    __suits = ["", "Clubs", "Diamonds", "Hearts", "Spades" ]

    
    def __str__(self):
        return f'Card({Card.__values[self.__value]} of {Card.__suits[self.__suit]}'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 cards.  if card1 == card2 for example.
            2 cards are equal if they're both cards and if their attributes have the same values"""
        if isinstance(other, Card):
            return self.__suit == other.suit and self.__value == other.value
        else:
            return False