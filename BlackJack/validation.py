# output styling
FAIL = '\033[91m'
END = '\033[0m'

def getInt(prompt = "Enter a whole number: "):
    """A function that gets and validates an integer from the user.
    It takes a string prompt, if provided, and returns an int value."""
    isValid = False

    # get input from user and validate that it's an integer
    while not isValid:
        try:
            # prompt user and set isValid to True if input is an integer
            value = int(input(prompt))
            isValid = True
        # throw exception if input is not an integer
        except ValueError:
            print("Invalid input. Input should be entered as a whole number.")

    return value

def getPositiveInt(prompt = "Enter a positive number: "):
    """A function that gets and validates a positive integer from the user.
    It takes a string prompt, if provided, and returns an int value."""
    isValid = False

    # get input from user and validate that it's a positive integer
    while not isValid:
        try:
            # prompt user and set isValid to true if input is a positive integer
            value = int(input(prompt))
            if value > 0:
                isValid = True
            else:
                print("Invalid input. Input should be greater than 0.")
        # throw exception if input is not an integer
        except ValueError:
            print("Invalid input. Input should be entered as a whole number.")

    return value

def getIntInRange(min, max, prompt = ""):
    """A function that gets and validates an integer that is within the specified range.
    It takes an int min, an int max, and a prompt, if provided, and returns an int value."""
    isValid = False

    # set default value for prompt if one is not provided
    if prompt == "":
        prompt = f"Enter a whole number between {min} and {max}: "

    # get input from user and validate that it's an integer and within range
    while not isValid:
        try:
            # prompt user and set isValid to true if input is a positive integer
            value = int(input(prompt))
            if value >= min and value <= max:
                isValid = True
            else:
                print(f"{FAIL}Out of range. Input must be between {min} and {max}{END}")
        # throw exception if input is not an integer
        except ValueError:
            print(f"{FAIL}Invalid input. Input should be entered as a whole number.{END}")

    return value

def getFloat(prompt = "Enter a floating point number: "):
    """A function that gets and validates a floating point number from the user.
    It takes a string prompt, if provided, and returns a float value."""
    isValid = False

    # get input from user and validate that it's a float
    while not isValid:
        try:
            # prompt user and set isValid to True if input is a float
            value = float(input(prompt))
            isValid = True
        # throw exception if input is not a float
        except ValueError:
            print("Invalid input. Input should be entered as a decimal number.")

    return value

def getPositiveFloat(prompt = "Enter a positive floating point number: "):
    """A function that gets and validates a positive floating point number from the user.
    It takes a string prompt, if provided, and returns a float value."""
    isValid = False

    # get input from user and validate that it's a positive float
    while not isValid:
        try:
            # prompt user and set isValid to True if input is a positive float
            value = float(input(prompt))
            isValid = True
        # throw exception if input is not a positive float
        except ValueError:
            print("Invalid input. Input should be entered as a positive decimal number.")

    return value