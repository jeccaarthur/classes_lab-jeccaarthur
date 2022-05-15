from boneyard import *

def testConstructor():
    b = Boneyard(6)
    print(f"Testing constructor.  Expect boneyard of 28 dominoes. {b}")
    print(f"Expect dominosRemaining property to be 28. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")

def testShuffle():
    b = Boneyard(6)
    b.shuffle()
    print(f"Testing shuffle.  Expect boneyard of 28 dominoes. {b}")
    print(f"Expect dominosRemaining property to be 28. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")

def testDraw():
    b = Boneyard(6)
    print(f"Testing draw.  Expect boneyard of 28 dominoes. {b}")
    print(f"Expect dominosRemaining property to be 28. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")
    d = b.draw()
    print(f"after call to deal.  Expect boneyard of 27 dominoes. {b}")
    print(f"Expect dominosRemaining property to be 27. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")
    print(f"Expect drawn domino to be 6 | 6. {d}")
    for i in range(b.dominosRemaining):
        d = b.draw()
    print(f"Drew the remaining dominoes.  Expect empty boneyard. {b}")
    print(f"Expect dominosRemaining property to be 0. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be true. {b.isEmpty}")

def testGetItem():
    b = Boneyard(6)
    print(f"Testing draw.  Expect boneyard of 28 dominoes. {b}")
    print(f"Expect dominosRemaining property to be 28. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")
    d = b[27]
    print(f"used [27].  Expect boneyard to remain the same. {b}")
    print(f"Expect dominosRemaining property to be 28. {b.dominosRemaining}")
    print(f"Expect isEmpty property to be false. {b.isEmpty}")
    print(f"Expect last domino to be 6 | 6. {d}")

def testIn():
    b = Boneyard(6)
    d1 = b.draw()
    print(f"Testing in.  Current unshuffled boneyard without 6 | 6. {b}")
    d2 = b[0]
    print(f"Is 6 | 6?  Expect false  {d1 in b}")
    print(f"Is 0 | 0 in the boneyard?  Expect true  {d2 in b}")

def testForLoop():
    b = Boneyard(6)
    print(f"Testing for loop.")
    print(f"Iterating through the boneyard with for in.  Expect 28 individual dominoes")
    for d in b:
        print(d)
