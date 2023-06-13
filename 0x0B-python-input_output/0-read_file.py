#!/usr/bin/python3
"""Define a function to read file"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to standard output"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
