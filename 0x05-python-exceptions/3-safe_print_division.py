#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of the division if successful, None otherwise.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
