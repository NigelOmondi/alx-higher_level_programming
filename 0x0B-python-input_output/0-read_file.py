#!/usr/bin/python3
"""Define a function to read file"""


def read_file(filename=""):
    """
    Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.

    Returns:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
