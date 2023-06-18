#!/usr/bin/python3


class Base:
    """
    Base class for managing the id attribute in all classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of instances.
        id (int): Public instance attribute representing the object's identifier.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The identifier for the object. Defaults to None.

        Notes:
            - If the id argument is provided, it will be assigned to the id attribute.
            - If the id argument is not provided, __nb_objects will be incremented
              and the new value will be assigned to the id attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
