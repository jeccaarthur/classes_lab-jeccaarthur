from customerList import *

c1 = ()
c2 = ()
c3 = ()
c4 = ()

def testConstructor():
    cList = CustomerList()
    print(f"Testing constructor. Expect empty list. {cList}")
    print(f"Expect count property to be 0. {cList.count}")
    print(f"Expect len function to be 0. {len(cList)}")

def testAppend():
    cList = CustomerList()
    c1 = Customer("test@email.com", "michael", "scott")
    c2 = Customer("secondtest@email.com", "dwight", "schrute")
    cList.append(c1)
    cList.append(c2)
    print(f"Testing append. Expect list with 2 customers. {cList}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")

def createList():
    # arrange customer list and customer objects
    cList = CustomerList()
    c1 = Customer("test@email.com", "michael", "scott")
    c2 = Customer("secondtest@email.com", "dwight", "schrute")
    c3 = Customer("thirdtest@email.com", "creed", "bratton")
    c4 = Customer("fourthtest@email.com", "kelly", "kapoor")
    cList.append(c1)
    cList.append(c2)
    cList.append(c3)
    return cList

def testFind():
    cList = createList()
    print(f"Testing find.  Current list with 3 customers. {cList}")
    index = cList.find("thirdtest@email.com")
    print(f"Called find with thirdtest@email.com as parameter.  Expect index to be 2. {index}")
    c2 = Customer("secondtest@email.com", "dwight", "schrute")
    # this will return -1 if __eq__ is not defined on the customer class
    index = cList.find(c2)
    print(f"Called find with dwight schrute Customer object as parameter.  Expect index to be 1. {index}")
    index = cList.find("wrong@email.com")
    print(f"Called find with wrong@email.com as parameter.  Expect index to be -1. {index}")
    index = cList.find(c4)
    print(f"Called find with kelly kapoor Customer object as parameter.  Expect index to be -1. {index}")

def testPop():
    cList = createList()
    print(f"Testing pop.  Before pop expect list with 3 customers. {cList}")
    print(f"Expect count property to be 3. {cList.count}")
    print(f"Expect len function to be 3. {len(cList)}")
    c3 = cList.pop()
    print(f"After pop with no parameter.  Expect first 2 customers. {cList}")
    print(f"Expect popped customer to be creed bratton. {c3}")
    print(f"Expect count property to be 2. {cList.count}")
    print(f"Expect len function to be 2. {len(cList)}")
    c1 = cList.pop(0)
    print(f"After pop with 0 parameter.  Expect just dwight schrute. {cList}")
    print(f"Expect popped customer to be michael scott. {c1}")
    print(f"Expect count property to be 1. {cList.count}")
    print(f"Expect len function to be 1. {len(cList)}")

def testRemove():
    cList = createList()
    c2 = Customer("secondtest@email.com", "dwight", "schrute")
    print(f"Testing find.  Current list with 3 customers. {cList}")
    cList.remove(c2)
    print(f"Called remove with dwight schrute Customer object as parameter.  Expect list to now have 2 customers. {cList}")
    c4 = Customer("fourthtest@email.com", "kelly", "kapoor")
    try:
        cList.remove(c4)
        print(f"Called remove with kelly kapoor Customer object as parameter.  An exception should have been thrown but was not.")
    except ValueError:
        print(f"Called remove with kelly kapoor Customer object as parameter.  An exception was expected and was thrown")
        print(f"Expect list to still have 2 customers. {cList}")

def testClear():
    cList = createList()
    print(f"Testing clear. Current list with 3 customers. {cList}")
    print()
    cList.clear()
    print(f"After the call to clear. Expect list to be empty. {cList}")

def testGetItem():
    cList = createList()
    print(f"Testing list access by index. Current list with 3 customers. {cList}")
    print()
    c = cList[1]
    print(f"Element at index 1. Expect dwight schrute. {c}")
    print()
    c = cList["thirdtest@email.com"]
    print(f"Element with key of thirdtest@email.com. Expect creed bratton. {c}")
    print()
    try:
        c = cList[2.5]
    except TypeError:
        print(f"Used [] with float as index.  An exception was expected and was thrown")

def testSetItem():
    cList = createList()
    print(f"Testing changing a list element by index.  Current list with 3 customers. {cList}")
    c4 = Customer("fourthtest@email.com", "kelly", "kapoor")
    cList[2] = c4
    print(f"Set element at index 2 to kelly kapoor.  kelly kapoor should be at the end of the list. {cList}")
    try:
        cList["fourthtest@email.com"] = c4
    except TypeError:
        print(f"Used [] with string as index.  An exception was expected and was thrown")
    try:
        cList[1] = "cat"
    except TypeError:
        print(f"Used [] with string element rather than a customer.  An exception was expected and was thrown")

def testIn():
    cList = createList()
    print(f"Testing in.  Current list with 3 customers. {cList}")
    c2 = Customer("secondtest@email.com", "dwight", "schrute")
    c4 = Customer("fourthtest@email.com", "kelly", "kapoor")
    print(f"Is dwight schrute in the list?  Expect true  {c2 in cList}")
    print(f"Is kelly kapoor in the list?  Expect false  {c4 in cList}")

def testForLoop():
    cList = createList()
    print(f"Testing for loop.  Current list with 3 customers. {cList}")
    print(f"Iterating through the list with for in.  Expect 3 individual customers")
    for c in cList:
        print(c)

def testAdd():
    cList = createList()
    cList2 = createList()
    cListCombined = cList + cList2
    print(f"Testing adding 2 customer lists.  Expect list with 6 customers. {cListCombined}")