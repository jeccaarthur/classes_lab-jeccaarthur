from hand import *
from bjhand import *
from deck import *

# region hand class tests
def testConstructor():
    h = Hand()
    d = Deck()
    print(f"Testing constructor - expecting empty hand of cards. {h}")

def testAddCard():
    h = Hand()
    d = Deck()
    print(f"Testing addCard")
    print(f"Before adding card - expecting numCards to be 0: {h.numCards}")
    h.addCard(d.deal())
    print(f"After adding card - expecting numCards to be 1: {h.numCards}")
    try:
        print(f"Checking with invalid parameter - expecting value error: {h.addCard(5)}")
    except ValueError as vErr:
        print(f"Checking with invalid parameter - an exception was expected and was thrown")
        print(vErr)

def testFillHand():
    h = Hand()
    d = Deck()
    print(f"Testing fillHand")
    print(f"Before filling hand - expecting empty hand: {h}")
    print(f"Before filling hand - expecting numCards to be 0: {h.numCards}")
    h.fillHand(5, d)
    print(f"After filling hand - expecting hand with 5 cards: {h}")
    print(f"After filling hand - expecting numCards to be 5: {h.numCards}")
    try:
        invalidString = "string"
        h.fillHand(invalidString, 3)
        print(f"Checking with invalid parameters - expecting value error")
    except ValueError as vErr:
        print(f"Checking with invalid parameters - an exception was expected and was thrown")
        print(vErr)

def testDiscard():
    h = Hand()
    d = Deck()
    h.fillHand(3, d)
    print(f"Testing discard")
    print(f"Hand before discard - expecting Ace, 2, and 3 of Clubs: {h}")
    print(f"Expecting numCards to be 3: {h.numCards}")
    print()
    c = h.discard(1)
    print(f"Hand after discard - expecting only Ace and 3 of Clubs: {h}")
    print(f"Expecting numCards to be 2: {h.numCards}")
    print(f"Expecting returned card to be 2 of Clubs: {c}")
    try:
        invalidString = "string"
        print(f"Checking with invalid parameter - expecting value error: {h.discard(invalidString)}")
    except ValueError as vErr:
        print(f"Checking with invalid parameter - an exception was expected and was thrown")
        print(vErr)

def testPrint():
    h = Hand()
    d = Deck()
    print(f"Testing string output")
    print(f"Before adding cards - expecting empty hand: {h}")
    h.fillHand(3, d)
    print(f"After adding cards - expecting hand with 3 cards: {h}")

def testIsEmpty():
    h = Hand()
    d = Deck()
    print(f"Testing addCard")
    print(f"Before adding card - expecting isEmpty property to be true. {h.isEmpty}")
    h.addCard(d.deal())
    print(f"After adding card - expecting isEmpty property to be false. {h.isEmpty}")

def testGetItem():
    h = Hand()
    d = Deck()
    h.fillHand(5, d)
    c = h[2]
    print(f"Testing indexer with h[2] - expecting 3 of Clubs: {c}")

def testIndexOf():
    h = Hand()
    d = Deck()
    h.fillHand(3, d)
    c1 = Card(1, 2)  # 2 of Clubs
    c2 = Card(2, 2)  # 2 of Diamonds
    print(f"Testing indexOf")
    print(f"Hand with 3 cards: {h}")
    print(f"Index of 2 of Clubs - expecting 1: {h.indexOf(c1)}")
    print(f"Index of card not in hand - expecting -1: {h.indexOf(c2)}")
    try:
        invalidString = "string"
        print(f"Checking with invalid parameter - expecting value error: {h.indexOf(invalidString)}")
    except ValueError as vErr:
        print(f"Checking with invalid parameter - an exception was expected and was thrown")
        print(vErr)

def testHasCard():
    h = Hand()
    d = Deck()
    h.fillHand(3, d)
    c1 = Card(1, 2)  # 2 of Clubs
    c2 = Card(2, 2)  # 2 of Diamonds
    print(f"Testing hasCard")
    print(f"Hand with 3 cards: {h}")
    print(f"Checking if 2 of Clubs is in hand - expecting true: {h.hasCard(c1)}")
    print(f"Checking if 2 of Diamonds is in hand - expecting false: {h.hasCard(c2)}")
    try:
        print(f"Checking with invalid parameter - expecting value error: {h.hasCard(5)}")
    except ValueError as vErr:
        print(f"Checking with invalid parameter - an exception was expected and was thrown")
        print(vErr)

def testHasCardWithSuit():
    h = Hand()
    d = Deck()
    h.fillHand(3, d)
    print(f"Testing hasCardWithSuit")
    print(f"Checking if hand contains Clubs - expecting true: {h.hasCardWithSuit(1)}")
    print(f"Checking if hand contains Diamonds - expecting false: {h.hasCardWithSuit(2)}")
    try:
        print(f"Checking with invalid suit - expecting value error: {h.hasCardWithSuit(5)}")
    except ValueError as vErr:
        print(f"Checking with invalid value - an exception was expected and was thrown")
        print(vErr)

def testHasCardWithValue():
    h = Hand()
    d = Deck()
    h.fillHand(3, d)
    print(f"Testing hasCardWithValue")
    print(f"Checking if hand contains an Ace - expecting true: {h.hasCardWithValue(1)}")
    print(f"Checking if hand contains a 5 - expecting false: {h.hasCardWithValue(5)}")
    try:
        print(f"Checking with invalid value - expecting value error: {h.hasCardWithValue(15)}")
    except ValueError as vErr:
        print(f"Checking with invalid value - an exception was expected and was thrown")
        print(vErr)

# endregion


# region bjhand tests

def testBJHandConstructor():
    b = BJHand()
    d = Deck()
    print(f"Testing constructor - expecting empty hand of cards. {b}")

def testHasAce():
    b = BJHand()
    d = Deck()
    b.fillHand(3, d)
    print(f"Testing hasAce")
    print(f"Hand with 3 cards including an ace: {b}")
    print(f"Result of hasAce - expecting true: {b.hasAce()}")
    b.discard(0)
    print(f"Result of hasAce after discarding ace - expecting false: {b.hasAce()}")

def testScoreAndIsBusted():
    d = Deck()
    b1 = BJHand()
    b1.fillHand(3, d)
    print(f"Testing score and isBusted")
    print(f"Current hand: {b1}")
    print(f"Score - expecting 16: {b1.score()}")
    print(f"isBusted - expecting false: {b1.isBusted()}")
    b2 = BJHand()
    b2.addCard(Card(1, 10))
    b2.addCard(Card(1, 12))
    print(f"Current hand: {b2}")
    print(f"Score - expecting 22: {b2.score()}")
    print(f"isBusted - expecting true: {b2.isBusted()}")


# endregion