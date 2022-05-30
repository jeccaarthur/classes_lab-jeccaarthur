from abc import ABC, abstractmethod
from domino import *
from hand import *


class Train(ABC):
    """ This class represents a train of dominos. It is and abstract base class for other train classes
        It contains one abstract method, isPlayable """

    def __init__(self, engineValue=12):
        """ Should create the empty list _dominos and initialize the _engineValue attribute """
        self._dominos = []
        self._engineValue = engineValue

    @property
    def count(self):
        """returns the number of dominos in the train"""
        return len(self._dominos)

    @property
    def engineValue(self):
        """returns the first playable value on the train"""
        return self._engineValue

    @property
    def isEmpty(self):
        """determines when the train is empty"""
        return self.count == 0

    @property
    def lastDomino(self):
        """ returns the last domino in the train or None when the train is empty """
        if self.isEmpty:
            return None
        else:
            return self._dominos[self.count - 1]

    @property
    def playableValue(self):
        """ returns side 2 of the last domino or the engine value """
        if self.isEmpty:
            return self.engineValue
        else:
            return self._dominos[self.count - 1].side2

    @abstractmethod
    def isPlayable(self, hand, domino):
        """ This abstract method takes a hand and a domino as its parameters and
        returns a tuple (isTheDominoPlayableByTheHand, mustTheDominoBeFlipped)
        DO NOT CHANGE THIS IMPLEMENTATION """
        pass

    def _isPlayable(self, domino):
        """ this protected method contains the logic for determining if a domino is playable on the train """
        if isinstance(domino, Domino):
            mustFlip = False
            okToPlay = False
            if self.playableValue == domino.side1:
                mustFlip = False
                okToPlay = True
            elif self.playableValue == domino.side2:
                mustFlip = True
                okToPlay = True
            else:
                pass
            return okToPlay, mustFlip
        else:
            raise TypeError(f"domino must be a valid domino object {type(domino)}  {domino}")

    def add(self, domino):
        """adds the user's selected domino to the train"""
        if isinstance(domino, Domino):
            self._dominos.append(domino)
        else:
            raise TypeError(f"Object must be a valid domino object")

    def play(self, hand, domino):
        """ this method plays a domino from a hand on the train.
        Notice that it calls the abstract method isPlayable even though it is not yet implemented. """
        if isinstance(hand, Hand) and isinstance(domino, Domino):
            okToPlay, mustFlip = self.isPlayable(hand, domino)
            if okToPlay:
                if mustFlip:
                    domino.flip()
                self.add(domino)
            else:
                raise ValueError(f"Domino {domino} does not match last domino in the train and can not be played")
        else:
            raise TypeError(f"hand and domino must be a valid hand and domino objects respectively {type(hand)}  {type(domino)}")

    def __str__(self):
        """creates a string representation of the train"""
        output = f"Train [\n" \
                 f""
        for d in self._dominos:
            output += d.__str__() + "\n"
        output += "]"
        return output

    def __getitem__(self, item):
        """allows use of indexer to get a domino in a train"""
        if isinstance(item, int):
            return self._dominos[item]
        else:
            raise TypeError(f"Index must an int")

    def __len__(self):
        """Allows a programmer to use the len function to get the length of a train"""
        return len(self._dominos)





