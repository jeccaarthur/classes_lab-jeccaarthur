from card import *

# output formatting
BOLD = '\033[1m'
END = '\033[0m'

def testConstructor():
    print(f"{BOLD}Testing constructor{END}")

    # arrange: instantiate a card
    c1 = Card(1, 10)

    # assert
    print(f"Expected: Ten of Clubs\n"
          f"Actual {c1}")

def testPropertyGetters():
    print(f"{BOLD}Testing getters{END}")

    # arrange: instantiate a card
    c1 = Card(1, 10)

    # assert
    print(f"Expected:\n"
          f"\tSuit: 1\n"
          f"\tValue: 10\n"
          f"Actual:\n"
          f"\tSuit: {c1.suit}\n"
          f"\tValue: {c1.value}")
    print()

def testPropertySetters():
    print(f"{BOLD}Testing setters{END}")

    # arrange: instantiate a card
    c1 = Card(1, 10)
    print(f"Card with initial values:\n"
          f"{c1}")
    print()

    # act: update attribute values
    c1.suit = 2
    c1.value = 12

    # assert
    print(f"Card with updated values:\n"
          f"Expected: Queen of Diamonds\n"
          f"Actual {c1}")
    print()

def testPropertySettersWithValidation():
    print(f"{BOLD}Testing setters with validation{END}")

    # arrange: instantiate a card
    c1 = Card(1, 10)

    # act: attempt to assign invalid values to each attribute
    # assert: appropriate exceptions should be thrown by each setter

    print(f"Suit:")
    try:  # not an int
        c1.suit = "boop"
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting suit to a string")
        print(f"\t{vErr}")
        print()
    try:  # int out of range
        c1.suit = 0
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting suit to an int out of range")
        print(f"\t{vErr}")
        print()

    print(f"Value:")
    try:  # not an int
        c1.value = "boop"
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting value to a string")
        print(f"\t{vErr}")
        print()
    try:  # int out of range
        c1.value = 0
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting value to an int out of range")
        print(f"\t{vErr}")
        print()

def testEquality():
    print(f"{BOLD}Testing equality{END}")

    # arrange: instantiate two cards with identical values
    c1 = Card(1, 10)
    c2 = Card(1, 10)

    print(f"Cards being compared:\n"
          f"{c1}\n"
          f"{c2}")
    print()

    # assert
    print(f"Comparison results:\n"
          f"Expected: True\n"
          f"Actual: {c1 == c2}")
    print()

def testEncapsulation():
    print(f"{BOLD}Testing encapsulation{END}")

    # arrange: instantiate a card
    c1 = Card(1, 10)

    # act: attempt to access private attributes
    # assert: appropriate exception should be thrown
    try: # get and set private attribute
        print(c1.__value)
        c1.__value = 3
        print(c1.__value)
        print(Card.__values)
    except AttributeError as attErr:
        print(f"An attribute error was thrown when attempting to access private attributes")
        print(attErr)
        print()

def testHasMatchingSuit():
    print(f"{BOLD}Testing suit comparison{END}")

    # arrange: instantiate two cards with the same suit
    c1 = Card(2, 3)
    c2 = Card(2, 5)

    print(f"Cards being compared:\n"
          f"\t{c1}\n"
          f"\t{c2}")
    print()

    # assert: call hasMatchingValue with both cards
    print(f"Comparison results:\n"
          f"\tExpected: True\n"
          f"\tActual: {c1.hasMatchingSuit(c2)}")
    print()

    # act: update one of the card suits
    c1.suit = 3

    print(f"Cards with updated suits:\n"
          f"\t{c1}\n"
          f"\t{c2}")
    print()

    # assert: call hasMatchingValue with updated cards
    print(f"Comparison results:\n"
          f"\tExpected: False\n"
          f"\tActual: {c1.hasMatchingSuit(c2)}")
    print()

def testHasMatchingValue():
    print(f"{BOLD}Testing value comparison{END}")

    # arrange: instantiate two cards with the same value
    c1 = Card(1, 3)
    c2 = Card(2, 3)

    print(f"Cards being compared:\n"
          f"\t{c1}\n"
          f"\t{c2}")
    print()

    # assert: call hasMatchingValue with both cards
    print(f"Comparison results:\n"
          f"\tExpected: True\n"
          f"\tActual: {c1.hasMatchingValue(c2)}")
    print()

    # act: update one of the card values
    c1.value = 5

    print(f"Cards with updated values:\n"
          f"\t{c1}\n"
          f"\t{c2}")
    print()

    # assert: call hasMatchingValue with updated cards
    print(f"Comparison results:\n"
          f"\tExpected: False\n"
          f"\tActual: {c1.hasMatchingValue(c2)}")
    print()

def testIsSuit():
    print(f"{BOLD}Testing suit identification{END}")

    # arrange: instantiate a card of each suit
    c1 = Card(1, 10)
    c2 = Card(2, 10)
    c3 = Card(3, 10)
    c4 = Card(4, 10)

    # assert: call each is{Suit} method for each card
    print(f"{c1}")
    print(f"\tIs Club: {c1.isClub()}\n"
          f"\tIs Diamond: {c1.isDiamond()}\n"
          f"\tIs Heart: {c1.isHeart()}\n"
          f"\tIs Spade: {c1.isSpade()}")
    print()

    print(f"{c2}")
    print(f"\tIs Club: {c2.isClub()}\n"
          f"\tIs Diamond: {c2.isDiamond()}\n"
          f"\tIs Heart: {c2.isHeart()}\n"
          f"\tIs Spade: {c2.isSpade()}")
    print()

    print(f"{c3}")
    print(f"\tIs Club: {c3.isClub()}\n"
          f"\tIs Diamond: {c3.isDiamond()}\n"
          f"\tIs Heart: {c3.isHeart()}\n"
          f"\tIs Spade: {c3.isSpade()}")
    print()

    print(f"{c4}")
    print(f"\tIs Club: {c4.isClub()}\n"
          f"\tIs Diamond: {c4.isDiamond()}\n"
          f"\tIs Heart: {c4.isHeart()}\n"
          f"\tIs Spade: {c4.isSpade()}")
    print()

def testIsColor():
    print(f"{BOLD}Testing color identification{END}")

    # arrange: instantiate a card of each suit
    c1 = Card(1, 10)
    c2 = Card(2, 10)
    c3 = Card(3, 10)
    c4 = Card(4, 10)

    # assert: call each is{Color} method for each card
    print(f"{c1} (black)")
    print(f"\tIs Black: {c1.isBlack()}\n"
          f"\tIs Red: {c1.isRed()}")
    print()

    print(f"{c2} (red)")
    print(f"\tIs Black: {c2.isBlack()}\n"
          f"\tIs Red: {c2.isRed()}")
    print()

    print(f"{c3} (red)")
    print(f"\tIs Black: {c3.isBlack()}\n"
          f"\tIs Red: {c3.isRed()}")
    print()

    print(f"{c4} (black)")
    print(f"\tIs Black: {c4.isBlack()}\n"
          f"\tIs Red: {c4.isRed()}")
    print()

def testIsAce():
    print(f"{BOLD}Testing isAce{END}")

    # arrange: instantiate an ace card
    c1 = Card(1, 1)

    # assert: call isAce
    print(f"Calling isAce with {c1}")
    print(f"\tExpected: True\n"
          f"\tActual: {c1.isAce()}")
    print()

    # act: update card value
    c1.value = 2

    # assert: call isAce with updated card
    print(f"Calling isAce with {c1}")
    print(f"\tExpected: False\n"
          f"\tActual: {c1.isAce()}")
    print()

def testIsFaceCard():
    print(f"{BOLD}Testing isFaceCard{END}")

    # arrange: instantiate four cards: jack, queen, king, and non-face
    c1 = Card(1, 11)
    c2 = Card(1, 12)
    c3 = Card(1, 13)
    c4 = Card(1, 3)

    # assert: call isFaceCard with each card
    print(f"Calling isAce with {c1}")
    print(f"\tExpected: True\n"
          f"\tActual: {c1.isFaceCard()}")
    print()

    print(f"Calling isAce with {c2}")
    print(f"\tExpected: True\n"
          f"\tActual: {c2.isFaceCard()}")
    print()

    print(f"Calling isAce with {c3}")
    print(f"\tExpected: True\n"
          f"\tActual: {c3.isFaceCard()}")
    print()

    print(f"Calling isAce with {c4}")
    print(f"\tExpected: False\n"
          f"\tActual: {c4.isFaceCard()}")
    print()