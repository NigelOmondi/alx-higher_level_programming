#!/usr/bin/python3
"""Define a function that writes to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.

    Args:
        filename (str): The name of the file to be written. Defaults to an empty string.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)
    return characters_written
