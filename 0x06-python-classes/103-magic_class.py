#!/usr/bin/python3

import math


class MagicClass:
    """
    A class representing a magic circle with radius.

    Attributes:
        __radius (float): The radius of the magic circle.
    """

    def __init__(self, radius):
        """
        Initialize a new MagicClass instance with the given radius.

        Args:
            radius (int or float): The radius of the magic circle.

        Raises:
            TypeError: If the radius is not a number (integer or float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return 2 * math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
