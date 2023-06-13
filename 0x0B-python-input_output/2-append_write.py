#!/usr/bin/python3
"""A function that appends to a text file"""


def append_write(filename="", text=""):
    """Returns the number of characters added to the end of a text file"""
    with open(filename, mode='a', encoding='utf=8') as file:
        return file.write(text)
