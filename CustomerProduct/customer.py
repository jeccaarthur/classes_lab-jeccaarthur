class Customer:
    """ This class represents a a customer.  It uses private attributes and property getters and setters.
        Setters have appropriate validation that raise an exception when invalid data is used."""

    def __init__(self, email = "na", firstName = "na", lastName = "na"):
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName

    @property
    def email(self):
        return self.__email

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName
    
    @email.setter
    def email(self, email):
        import re
        # validate that the provided value is a string and matches email format
        if not isinstance(email, str) or len(email.strip()) == 0:  # not a string or empty string
            raise ValueError(f"Email must be a non-empty character string.")
        elif not re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email.strip()):   # incorrect format
            raise ValueError(f"Invalid email format.")
        else:   # valid string in correct format
            self.__email = email.strip()

    @firstName.setter
    def firstName(self, firstName):
        # validate that provided value is not an empty string
        if isinstance(firstName, str) and len(firstName.strip()) > 0:
            self.__firstName = firstName.strip()
        else:
            raise ValueError(f"First name must be a non-empty character string.")

    @lastName.setter
    def lastName(self, lastName):
        # validate that provided value is not an empty string
        if isinstance(lastName, str) and len(lastName.strip()) > 0:
            self.__lastName = lastName.strip()
        else:
            raise ValueError(f"Last name must be a non-empty character string.")

    def __str__(self):
        return f"Customer:\n" \
               f"\tEmail: {self.__email}\n" \
               f"\tFirst name: {self.__firstName}\n" \
               f"\tLast name: {self.lastName}"

    def __eq__(self, other):
        """Checks equality of two customer objects"""
        if isinstance(other, Customer):
            return self.__email == other.email \
                   and self.__firstName == other.firstName \
                   and self.__lastName == other.lastName
        else:
            return False