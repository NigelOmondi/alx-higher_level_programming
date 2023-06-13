#!/usr/bin/python3
"""A function that appends to a text file"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file and return the number of characters added.

    Args:
        filename (str): The name of the file to which the string will be appended. Defaults to an empty string.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_added = file.write(text)
    return characters_added
