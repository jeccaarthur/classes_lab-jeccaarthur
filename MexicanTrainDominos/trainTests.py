from mexicanTrain import *
from playerTrain import *

# these global variables can be used for testing
mTrain1 = MexicanTrain()
mTrain2 = MexicanTrain(6)
h = Hand()
hOther = Hand()
pTrain = PlayerTrain(h, 12)
d12_1 = Domino(12, 1)
d1_12 = Domino(1, 12)
d3_4 = Domino(3, 4)
d1_6 = Domino(1, 6)

# this function resets each of the globals to a known state
def resetGlobals():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    mTrain1 = MexicanTrain()
    mTrain2 = MexicanTrain(6)
    h = Hand()
    hOther = Hand()
    pTrain = PlayerTrain(h, 12)
    d12_1 = Domino(12, 1)
    d1_12 = Domino(1, 12)
    d1_6 = Domino(1, 6)
    d3_4 = Domino(3, 4)


def testAdd():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print("Testing add")
    print(f"Train before adding anything to it – expecting empty train: {mTrain1}")
    mTrain1.add(d12_1)
    print(f"Train after add – expecting one domino: {mTrain1}")


def testPlayOnMexicanTrain():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    okToPlay, mustFlip = mTrain1.isPlayable(h, d1_12)
    print(f"Testing with 1 | 12 - expecting True, True: {okToPlay}, {mustFlip}")
    okToPlay, mustFlip = mTrain1.isPlayable(h, d12_1)
    print(f"Testing with 12 | 1 - expecting True, False: {okToPlay}, {mustFlip}")
    okToPlay, mustFlip = mTrain1.isPlayable(h, d3_4)
    print(f"Testing with 3 | 4 - expecting False, False: {okToPlay}, {mustFlip}")

    print(f"Before play")
    print(f"Last domino – expecting None: {mTrain1.lastDomino}")
    print(f"Playable value – expecting 12: {mTrain1.playableValue}")
    print(f"Count – expecting 0: {mTrain1.count}")
    mTrain1.play(h, d1_12)
    print(f"After play")
    print(f"Last domino – expecting 12 | 1: {mTrain1.lastDomino}")
    print(f"Playable value – expecting 1: {mTrain1.playableValue}")
    print(f"Count – expecting 1: {mTrain1.count}")
    try:
        mTrain1.play(h, d3_4)
    except ValueError as rErr:
        print("Attempting to play with unplayable value - expecting exception")
        print(rErr)
        # print last domino and playable value and count and make sure they haven't changed
        print(f"Last domino – expecting 12 | 1: {mTrain1.lastDomino}")
        print(f"Playable value – expecting 1: {mTrain1.playableValue}")
        print(f"Count – expecting 1: {mTrain1.count}")
    print()


def testPlayOnPlayerTrain():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    okToPlay, mustFlip = pTrain.isPlayable(h, d1_12)
    print(f"Testing with 1 | 12 and matching hand - expecting True, True: {okToPlay}, {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(h, d12_1)
    print(f"Testing with 12 | 1 and matching hand - expecting True, False: {okToPlay}, {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(h, d3_4)
    print(f"Testing with 3 | 4 and matching hand - expecting False, False: {okToPlay}, {mustFlip}")
    okToPlay, mustFlip = pTrain.isPlayable(hOther, d1_12)
    print(f"Testing with 1 | 12 and mismatched hand - expecting False, False: {okToPlay}, {mustFlip}")
    pTrain.open()
    okToPlay, mustFlip = pTrain.isPlayable(hOther, d1_12)
    print(f"Testing with 1 | 12, mismatched hand, and open train - expecting True, True: {okToPlay}, {mustFlip}")
    print()


# just so you know how to use the globals and resetGlobal
def testMTConstructor():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()
    # the rest of your test will go here

    print(f"Testing constructor")
    print(f"Expecting empty train: {mTrain1}")
    print(f"Constructor with default param - expecting engine value of 12: {mTrain1.engineValue}")
    print(f"Constructor with engine value - expecting engine value of 6: {mTrain2.engineValue}")


def testCount():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing count")
    print(f"Before adding to train - expecting 0: {mTrain1.count}")
    mTrain1.add(d12_1)
    print(f"After adding to train - expecting 1: {mTrain1.count}")


def testIsEmpty():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing isEmpty")
    print(f"Before adding to train - expecting true: {mTrain1.isEmpty}")
    mTrain1.add(d12_1)
    print(f"After adding to train - expecting false: {mTrain1.isEmpty}")


def testLastDomino():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing lastDomino")
    mTrain1.add(d12_1)
    mTrain1.add(d1_12)
    print(mTrain1)
    print(f"Expecting last domino to be 1 | 12: {mTrain1.lastDomino}")


def testPlayableValue():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing playableValue")
    print(mTrain1)
    print(f"Empty train - expecting 12: {mTrain1.playableValue}")

    mTrain2.add(d1_12)
    mTrain2.add(d12_1)
    mTrain2.add(d1_6)
    print(mTrain2)
    print(f"Train with dominos - expecting 6: {mTrain2.playableValue}")


def testGetItem():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    mTrain1.add(d12_1)
    mTrain1.add(d1_12)
    mTrain1.add(d3_4)

    print(f"Testing getitem")
    print(mTrain1)
    print(f"Retrieving mTrain1[1] - expecting 1 | 12: {mTrain1[1]}")


def testOpenAndClose():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing open and close")
    print(f"Testing default player train state - expecting false: {pTrain.isOpen}")
    pTrain.open()
    print(f"After opening - expecting true: {pTrain.isOpen}")
    pTrain.close()
    print(f"After closing - expecting false: {pTrain.isOpen}")


def testMtIsPlayable():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing MT isPlayable")
    mTrain1.add(d12_1)
    print(mTrain1)
    print(f"Testing with 1 | 12 - expecting True (okToPlay), False (mustFlip): "
          f"{mTrain1.isPlayable(h, d1_12)}")

    print(f"Testing with 3 | 4 - expecting False (okToPlay), False (mustFlip): "
          f"{mTrain1.isPlayable(h, d3_4)}")

    print(f"Testing with 12 | 1 - expecting True (okToPlay), True (mustFlip): "
          f"{mTrain1.isPlayable(h, d12_1)}")


def testPtIsPlayable():
    global mTrain1, mTrain2, h, hOther, pTrain, d12_1, d1_12, d3_4, d1_6
    resetGlobals()

    print(f"Testing PT isPlayable")
    pTrain.add(d12_1)
    print(pTrain)

    pTrain.open()
    print(f"Testing with 1 | 12, matching hand, and open train - expecting True (okToPlay), False (mustFlip): "
          f"{pTrain.isPlayable(h, d1_12)}")
    print(f"Testing with 1 | 12, mismatched hand, and open train - expecting True (okToPlay), False (mustFlip): "
          f"{pTrain.isPlayable(hOther, d1_12)}")
    pTrain.close()
    print(f"Testing with 1 | 12, matching hand, and closed train - expecting True (okToPlay), False (mustFlip): "
          f"{pTrain.isPlayable(h, d1_12)}")
    print(f"Testing with 1 | 12, mismatched hand, and closed train - expecting False (okToPlay), False (mustFlip): "
          f"{pTrain.isPlayable(hOther, d1_12)}")



