#!/usr/bin/python3
""" Defines a class named square """

class Square:
    """ This class defines a square with a private instance
        attribute called, size.
    """

    def __init__(self, size):

        """Initializes a square instance with the given size.

            Args:
                size(int): The size of the square.
        """
        self.__size = size
