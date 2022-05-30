from train import *


class MexicanTrain(Train):
    """ this class represents the mexican train.  It is derived from the abstract Train class.
    It MUST implement the abstract method isPlayable. """

    def __init__(self, engineValue=12):
        """creates a mexican train object"""
        super().__init__(engineValue)

    def isPlayable(self, playerHand, domino):
        """determines if a domino is playable on the train"""
        return self._isPlayable(domino)