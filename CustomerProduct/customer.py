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
        # validate that provided value matches email format
        if re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"):
            self.__email = email.strip()
        else:
            raise ValueError(f"Invalid email format. {email}")

    @firstName.setter
    def firstName(self, firstName):
        # validate that provided value is not an empty string
        if isinstance(firstName, str) and len(firstName.strip()) > 0:
            self.__firstName = firstName.strip()
        else:
            raise ValueError(f"First name must be a non-empty character string. {firstName}")

    @lastName.setter
    def lastName(self, lastName):
        # validate that provided value is not an empty string
        if isinstance(lastName, str) and len(lastName.strip()) > 0:
            self.__firstName = lastName.strip()
        else:
            raise ValueError(f"Last name must be a non-empty character string. {lastName}")

    def __str__(self):
        return f'Customer(email: {self.__email}, first name: {self.__firstName}, last name: {self.lastName})'