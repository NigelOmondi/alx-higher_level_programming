#!/usr/bin/python3
""" Definition of class Square """


class Square:
    """
    Defines a square with a private instance attribute called 'size'.

    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
