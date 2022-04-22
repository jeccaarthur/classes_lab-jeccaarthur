from domino import *


def testConstructor():
    d = Domino(1, 2)
    print(f"Testing constructor with parameters.  Expect domino 1 | 2 {d}")


def testPropertyGetters():
    d = Domino(1, 2)
    print(f"Testing property getters.  Expect individual attributes for domino 1 | 2")
    print(f"side1: {d.side1}, side2: {d.side2}, score: {d.score}")


def testPropertySetters():
    d = Domino(1, 2)
    d.side1 = 3
    d.side2 = 12
    print(f"Testing property setters.  Expect individual attributes for domino 1|2 to change to 3|12. {d}")

def testPropertySettersWithValidation():
    d = Domino(1, 2)
    try:
        d.side1 = "3"
    except ValueError as vErr:
        print ("An exception was thrown setting side1 to a string")
        print(vErr)
    try:
        d.side1 = 15
    except ValueError as vErr:
        print ("An exception was thrown setting side1 to 15")
        print(vErr)
    try:
        d.side2 = "3"
    except ValueError as vErr:
        print ("An exception was thrown setting side2 to a string")
        print(vErr)
    try:
        d.side2 = -1
    except ValueError as vErr:
        print ("An exception was thrown setting side2 to -1")
        print(vErr)

def testEncapsulation():
    d = Domino(1, 2)
    try:
        print (d.__side1)
    except AttributeError as attErr:
        print("An attribute error was throws in testEncapsultion")
        print(attErr)

def testIsDouble():
    d = Domino(6, 6)
    print(f"Testing is double.  Expect is double for domino 6|6 to return true. {d.isDouble()}")
    d.side2 = 3
    print(f"Testing is double.  Expect is double for domino 6|3 to return false. {d.isDouble()}")

def testFlip():
    d = Domino(1, 2)
    print(f"Testing flip.  Expect 1|2 before flip. {d}")
    d.flip()
    print(f"Testing flip.  Expect 2|1 after flip. {d}")

def testEquals():
    d1 = Domino(1, 2)
    d2 = Domino(1, 2)
    d3 = Domino(1, 3)
    print(f"Testing equality.  Expect 1|2 and 1|2 to be equal {d1 == d2}")
    print(f"Testing equality.  Expect 1|2 and 1|3 to NOT be equal {d1 == d3}")
