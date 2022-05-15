'''
A boneyard contains a list of domino objects.
A programmer must be able to create a boneyard by providing the
maximum number of dots on the side of any domino.
When the boneyard is created it should create all of the domino objects
and add them to the list.

A boneyard must be able to:
* get its number of dominos remaining
* get a domino based on its position in the boneyard
* draw or deal a domino from the top of the boneyard
* get whether it is empty or not
* shuffle itself
* convert its attributes to a string for displaying on the screen
* use the in operator to see if a domino is in the boneyard
* use a for loop to iterate through the dominos in the boneyard
'''

from domino import *
from random import randint

class Boneyard:
    """This class represents a 'deck' of dominos"""

    def __init__(self, maxDots = 12):
        """Creates a list of dominos from 0, 0 up to and including maxDots, maxDots"""
        self.__dominos = []
        for side1 in range(0, maxDots + 1):
            for side2 in range (side1, maxDots + 1):
                self.__dominos.append(Domino(side1, side2))

    @property
    def isEmpty(self):
        """Determines when the list of dominos is empty"""
        return len(self.__dominos) == 0

    @property
    def dominosRemaining(self):
        """Returns the number of dominos remaining in the list"""
        return len(self.__dominos)

    def shuffle(self):
        """Shuffles the list of dominos"""
        for i in range(self.dominosRemaining):
            rndIndex = randint(0, self.dominosRemaining - 1)
            self.__dominos[i], self.__dominos[rndIndex] = self.__dominos[rndIndex], self.__dominos[i]

    def draw(self):
        """Returns the 'top' domino in the boneyard.  Removes the domino from the list"""
        if not self.isEmpty:
            d = self.__dominos.pop(self.dominosRemaining - 1)
            return d
        else:
            return None

    def find(self, item):
        if isinstance(item, Domino):
            index = 0
            for domino in self.__dominos:
                if domino == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    def append(self, item):
        if isinstance(item, Domino):
            self.__dominos.append(item)
        else:
            raise TypeError(f"Object must be a valid customer object {type(item)}  {item}")

    def __getitem__(self, item):
        """Allows a programmer to use [] to peek at a domino in the middle of the boneyard"""
        if isinstance(item, int):
            return self.__dominos[item]
        else:
            raise TypeError(f"Index must an int {type(item)}  {item}")

    def __str__(self):
        """Creates a string representation of the boneyard"""
        output = f"\nBoneyard\n[\n"
        for domino in self.__dominos:
            output += domino.__str__() + "\n"
        output += "]"
        return output

    def __len__(self):
        """Allows a programmer to use the len function to get the length of a domino list"""
        return len(self.__dominos)

    def __delitem__(self, key):
        """Allows a programmer to use del to delete an element from a list of dominos"""
        if isinstance(key, int):
            del self.__dominos[key]
        else:
            raise TypeError(f"Index must an int {type(key)}  {key}")
