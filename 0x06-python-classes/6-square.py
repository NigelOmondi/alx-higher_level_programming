#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    A class representing a square.

    This class defines a square with private instance
    attributes 'size' and 'position'.
    The size and position of the square are crucial for various
    computations and are kept private
    to ensure control over their types and values.
    The size must be a non-negative integer,
    and the position must be a tuple of 2 positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer, or if position is
            not a tuple.
            ValueError: If size is less than 0, or if position
            does not contain 2 positive integers.

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If position is not a tuple.
            ValueError: If position does not contain 2 positive integers.

        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(x, int)
and x >= 0 for x in value):
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' in stdout.

        If size is equal to 0, prints an empty line.
        The position is used to offset the square 
	horizontally and vertically.

        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
