#!/usr/bin/python3
"""Module Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    """
    A class that prevents dynamic creation of new instance attributes,
    except for the attribute 'first_name'.
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        Intercept attribute assignments and raise an AttributeError
        if the attribute being assigned is not 'first_name' or
        already exists in the instance.
        """

        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        object.__setattr__(self, name, value)
