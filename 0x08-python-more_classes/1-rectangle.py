#!/usr/bin/python3
"""Create a class, Rectangle"""


class Rectangle:
    """Define the rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle with a given width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter method for retrieving the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter method to set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """A getter method to retrieve rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter method to set height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
