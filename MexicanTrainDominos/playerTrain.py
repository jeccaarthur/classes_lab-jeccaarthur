from train import *
from hand import *


class PlayerTrain(Train):
    """ this class represents the player train.  It is derived from the abstract Train class.
    It MUST implement the abstract method isPlayable. It has 2 new instance variables --
    the hand(player) to which it belongs and a flag that determines if the train is currently open """

    def __init__(self, hand, engineValue=12):
        """creates a player train object"""
        super().__init__(engineValue)
        self.__hand = hand
        self.__isOpen = False

    @property
    def isOpen(self):
        """returns true if the player train is open"""
        return self.__isOpen

    def open(self):
        """opens the player train"""
        self.__isOpen = True

    def close(self):
        """closes the player train"""
        self.__isOpen = False

    def isPlayable(self, playerHand, domino):
        """determines if a domino is playable on the train"""
        if isinstance(playerHand, Hand) and isinstance(domino, Domino):
            if self.__hand == playerHand or self.isOpen:
                return self._isPlayable(domino)
            else:
                return False, False
        else:
            raise TypeError(f"Objects provided must be a valid hand and a valid domino")





