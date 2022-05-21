from card import *
from deck import *
from handTests import *
from bjhand import *

def main():
    """blackjack"""

    # bjHand tests
    testBJHandConstructor()
    print()
    testHasAce()
    print()
    testScoreAndIsBusted()
    print()

    '''
    # hand tests
    testConstructor()
    print()
    testAddCard()
    print()
    testFillHand()
    print()
    testPrint()
    print()
    testIsEmpty()
    print()
    testGetItem()
    print()
    testDiscard()
    print()
    testIndexOf()
    print()
    testHasCard()
    print()
    testHasCardWithSuit()
    print()
    testHasCardWithValue()
    print()
    '''

    '''
    # card tests
    testConstructor()
    testPropertyGetters()
    testPropertySetters()
    testPropertySettersWithValidation()
    testEquality()
    testEncapsulation()
    testHasMatchingSuit()
    testHasMatchingValue()
    testIsSuit()
    testIsColor()
    testIsAce()
    testIsFaceCard()
    '''

if __name__ == '__main__':
    main()
