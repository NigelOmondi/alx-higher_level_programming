#!/usr/bin/python3
"""Define a function that writes to a file"""


def write_file(filename="", text=""):
    """returns the number of chars written to "filename" from "text" """
    with open(filename, mode='w', encoding='utf=8') as file:
        return file.write(text)
