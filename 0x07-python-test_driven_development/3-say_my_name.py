#!/usr/bin/python3
"""Module prints a full name"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + last_name
    if last_name:
        full_name = first_name + " " + last_name
    else:
        full_name = first_name + " "
    print("My name is", full_name)
