'''
A customer list contains a list of customer objects.
It should provide the same functionality that is provided in the
ProductList class.  A programmer must be able to create a customer
list without providing any additional information.

A customer list must be able to:
* get its count
* use the predefined len() function to get the length of the list
* get a customer based on its position in the list
* change the customer object in a specific position in the list
* get a customer based on its email address
* append a customer object
* pop the last customer from the list
* pop a customer at a particular index from the list
* remove a customer based on a customer object
* convert its attributes to a string for displaying on the screen
* use the in operator to see if a customer object is in the customer list
* use a for loop to iterate through the customer list
'''

from customer import *

class CustomerList:
    """This class represents a list of customer objects"""

    # region: constructor :
    def __init__(self):
        self.__customers = []
    # endregion

    # region: properties :
    # get list count
    @property
    def count(self):
        return len(self.__customers)
    # endregion

    # region: methods :

    # append customer to list
    def append(self, item):
        if isinstance(item, Customer):
            self.__customers.append(item)
        else:
            raise TypeError(f"Object must be a valid customer object {type(item)}  {item}")

    # clear list
    def clear(self):
        self.__customers = []

    # find customer in list
    def find(self, item):
        if isinstance(item, Customer):
            index = 0
            for customer in self.__customers:
                if customer == item:
                    return index
                index += 1
            return -1
        elif isinstance(item, str):
            index = 0
            for customer in self.__customers:
                if customer.email == item:
                    return index
                index += 1
            return -1
        else:
            return -1

    # pop customer from list (with index)
    def pop(self, index=None):
        if index is None:
            return self.__customers.pop()
        else:
            return self.__customers.pop(index)

    # remove customer from list (with customer)
    def remove(self, item):
        index = self.find(item)
        if index == -1:
            raise ValueError(f"{item} is not in the customer list")
        else:
            self.pop(index)

    # endregion

    # region: magic methods :

    # override str to display a list of customers
    def __str__(self):
        output = f"\nCustomerList\n[\n"
        for customer in self.__customers:
            output += customer.__str__() + "\n"
        output += "]"
        return output

    # override getitem to get customer by index or email
    # this allows use of indexer
    def __getitem__(self, item):
        """Allows a programmer to [] to get an element in a customer list"""
        if isinstance(item, int):
            return self.__customers[item]
        elif isinstance(item, str):
            return self.__customers[self.find(item)]
        else:
            raise TypeError(f"Index must an int or an email address {type(item)}  {item}")

    # override setitem to mutate customer in list
    def __setitem__(self, key, value):
        """Allows a programmer to [] to mutate an element in a customer list"""
        if isinstance(key, int) and isinstance(value, Customer):
            self.__customers[key] = value
        elif not isinstance(key, int):
            raise TypeError(f"Index must an int {type(key)}  {key}")
        elif not isinstance(value, Customer):
            raise TypeError(f"Item must a Customer object {type(value)}  {value}")

    # override len to get list length
    def __len__(self):
        """Allows a programmer to use the len function to get the length of a customer list"""
        return len(self.__customers)

    # override delitem remove specified customer from list
    def __delitem__(self, key):
        """Allows a programmer to use del to delete an element from a customer list"""
        if isinstance(key, int):
            del self.__customers[key]
        else:
            raise TypeError(f"Index must an int {type(key)}  {key}")

    # override add to concatenate lists
    def __add__(self, other):
        """Allows concatenation of customer lists.
        Does not make a copy of the individual customers."""
        if isinstance(other, CustomerList):
            newList = CustomerList()
            for c in self.__customers:
                newList.append(c)
            for c in other.__customers:
                newList.append(c)
            return newList
        else:
            raise TypeError(f"Other must a customer list {type(other)}  {other}")

    #endregion















