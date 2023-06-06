#!/usr/bin/python3
"""Module Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        object.__setattr__(self, name, value)
