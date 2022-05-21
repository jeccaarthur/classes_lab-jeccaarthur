from hand import *

class BJHand(Hand):
    """represents a blackjack hand. inherits from hand class."""

    def __init__(self):
        """constructor that creates an empty blackjack hand"""
        super().__init__()

    def hasAce(self):
        """returns true when a hand contains an ace card"""
        return self.hasCardWithValue(1)

    def isBusted(self):
        """returns true if score is greater than 21"""
        return self.score() > 21

    def score(self):
        """calculates and returns a hand's score"""
        handScore = 0

        for card in self:
            if card.isFaceCard():
                handScore += 10
            else:
                handScore += card.value

        if self.hasAce() and handScore <= 11:
            handScore += 10

        return handScore

