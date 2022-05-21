from productBest import *
from gear import *
from clothing import *
from productList import *

def testGearConstructor():
    g1 = Gear(5, "G100", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32);
    print(f"Testing gear constructor.  Expecting 5, g100, etc \n {g1}")

def testClothingConstructor():
    c1 = Clothing(3, "C100", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    print(f"Testing clothing constructor.  Expecting 3, c100, etc \n {c1}")

def testEqWithInheritance():
    p1 = Product(1, "T100", "This is a test product", 100, 10)
    p2 = Product(1, "T100", "This is a test product", 100, 10)
    c1 = Clothing(3, "C100", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    c2 = Clothing(3, "C100", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    c3 = Clothing(3, "C100", "Running tights", 69.99, 3, "not pants", "Lucy", "womens", "large", "blue")
    g1 = Gear(5, "G100", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    g2 = Gear(5, "G100", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    g3 = Gear(1, "T100", "This is a test product", 100, 10, "paddle", "Eddyline", "plastic laminate", 32)
    # this is an example of polymorphism.  == calls the right version of __eq__ depending on the object type
    print("Testing product ==.")
    print(f"2 products that have the same properties should be equal.  Expecting true. {p1 == p2}")
    print(f"2 clothing that have the same properties should be equal.  Expecting true. {c1 == c2}")
    print(f"2 gear that have the same properties should be equal.  Expecting true. {g1 == g2}")
    print(f"Product and Gear should not be equal.  Expecting false. {p1 == g3}")
    print(f"2 clothing that have the same product attributes should not be equal.  Expecting false. {c1 == c3}")


def testProductListWithInheritance():
    p1 = Product(1, "T100", "This is a test product", 100, 10)
    p2 = Product(2, "T200", "This is a test product", 100, 10)
    c1 = Clothing(3, "C100", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    c2 = Clothing(4, "C200", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    g1 = Gear(5, "G100", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    g2 = Gear(6, "G200", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    pList = ProductList()
    # this is an example of polymorphism.  I can put any kind of product in a product list.
    pList.append(p1)
    pList.append(p2)
    pList.append(c1)
    pList.append(c2)
    pList.append(g1)
    pList.append(g2)

    print("Testing product list with gear and clothing.")
    for p in pList:
        print(p)
