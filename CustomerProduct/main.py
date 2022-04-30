import productTests
import customerTests

def main():
    # product tests
    # productTests.testConstructor()
    # print()
    #productTests.testGetters()
    # productTests.testPropertyGetters()
    #productTests.testSetters()
    # productTests.testPropertySetters()
    # print()
    # productTests.testPropertySettersWithValidation()
    # print()
    # productTests.testEncapsulation()
    print()


    # customer tests
    customerTests.testConstructor()
    print()
    customerTests.testPropertyGetters()
    print()
    customerTests.testPropertySetters()
    print()
    customerTests.testPropertySettersWithValidation()
    print()
    customerTests.testEncapsulation()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()