from customer import *

# output formatting
BOLD = '\033[1m'
END = '\033[0m'

def testConstructor():
    print(f"{BOLD}Testing constructor with default values{END}")
    # arrange: instantiate a customer with default values
    c1 = Customer()

    # assert
    print(f"Expected:\n"
          f"\tEmail: na\n"
          f"\tFirst name: na\n"
          f"\tLast name: na\n"
          f"Actual {c1}")
    print()

    print(f"{BOLD}Testing constructor with provided values{END}")
    # arrange: instantiate a customer with provided values
    c2 = Customer("hello@test.com", "test", "user")

    # assert
    print(f"Expected:\n"
          f"\tEmail: hello@test.com\n"
          f"\tFirst name: test\n"
          f"\tLast name: user\n"
          f"Actual {c2}")
    print()

def testPropertyGetters():
    print(f"{BOLD}Testing getters{END}")

    # arrange: instantiate a customer with provided values
    c1 = Customer("hello@test.com", "test", "user")

    # assert
    print(f"Expected:\n"
          f"\tEmail: hello@test.com\n"
          f"\tFirst name: test\n"
          f"\tLast name: user\n"
          f"Actual:\n"
          f"\tEmail: {c1.email}\n"
          f"\tFirst name: {c1.firstName}\n"
          f"\tLast name: {c1.lastName}")
    print()

def testPropertySetters():
    print(f"{BOLD}Testing setters{END}")

    # arrange: instantiate a customer with provided values
    c1 = Customer("hello@test.com", "test", "user")
    print(f"Customer with initial values:\n"
          f"{c1}")
    print()

    # act: update attribute values
    c1.email = "newemail@test.com"
    c1.firstName = "new"
    c1.lastName = "name"

    # assert
    print(f"Customer with updated values:\n"
          f"Expected:\n"
          f"\tEmail: newemail@test.com\n"
          f"\tFirst name: new\n"
          f"\tLast name: name\n"
          f"Actual {c1}")
    print()

def testPropertySettersWithValidation():
    print(f"{BOLD}Testing setters with validation{END}")

    # arrange: instantiate a customer with provided values
    c1 = Customer("hello@test.com", "test", "user")

    # act: attempt to assign invalid values to each attribute
    # assert: appropriate exceptions should be thrown by each setter

    print(f"Email:")
    try:  # invalid format
        c1.email = "fakeemail@somedomain"
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting email with invalid format: fakeemail@somedomain")
        print(f"\t{vErr}")
        print()
    try:  # empty string
        c1.email = "  "
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting email to an empty string")
        print(f"\t{vErr}")
        print()
    try:  # not a string
        c1.email = 20
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting email to an int")
        print(f"\t{vErr}")
        print()

    print(f"First name:")
    try:  # empty string
        c1.firstName = "  "
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting first name to an empty string")
        print(f"\t{vErr}")
        print()
    try:  # not a string
        c1.firstName = 20
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting first name to an int")
        print(f"\t{vErr}")
        print()

    print(f"Last name:")
    try:  # empty string
        c1.lastName = "  "
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting last name to an empty string")
        print(f"\t{vErr}")
        print()
    try:  # not a string
        c1.lastName = 20
    except ValueError as vErr:
        print(f"\tAn exception was thrown setting last name to an int")
        print(f"\t{vErr}")
        print()

def testEncapsulation():
    print(f"{BOLD}Testing encapsulation{END}")

    # arrange: instantiate a customer with provided values
    c1 = Customer("hello@test.com", "test", "user")

    # act: attempt to access private attributes
    # assert: appropriate exception should be thrown
    try:  # get and set private attribute
        print(c1.__email)
        c1.__email = "newemail@domain.com"
        print(c1.__email)
    except AttributeError as attErr:
        print("An attribute error was thrown when attempting to access private attributes")
        print(AttributeError)
        print()







