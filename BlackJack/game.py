def getPhrase(prompt = "Enter a word or phrase: "):
    """A function that gets string input from the user.
    It takes no parameters and returns a string userInput."""
    isValid = False

    # get input from user
    userInput = input(prompt)

    return userInput

def playAgain(prompt = "Enter 'yes' to play again, or enter anything else to quit: "):
    """A function that asks the user if they'd like to play again.
    It takes no parameters and returns a bool repeat."""
    # prompt user
    userInput = input(prompt)

    # convert to lower
    userInput = userInput.lower()

    if userInput == "yes":
        repeat = True
    else:
        repeat = False

    return repeat

def generateRandomNumber(min, max):
    """A function that generates a random number between the specified minimum and maximum.
    It takes an int min and an int max and returns an int number."""
    import random

    number = random.randint(min, max)

    return number