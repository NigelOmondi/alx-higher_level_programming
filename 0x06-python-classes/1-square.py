#!/usr/bin/python3
"""Definition of class Square"""

class Square:
    """ Declares a square class """

    def __init__(self, size) -> None:
        """
        Initializes class attributes

        Args:
            size: size of square
        """
        self.__size = size
