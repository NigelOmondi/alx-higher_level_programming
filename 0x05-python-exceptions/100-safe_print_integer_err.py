#!/usr/bin/python3


import sys


def safe_print_integer_err(value):
    """Prints an integer and handles errors.

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and
        has been printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
