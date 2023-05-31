#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        *args: Variable-length argument list.

    Returns:
        The result of the function if executed successfully, None otherwise.
    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
