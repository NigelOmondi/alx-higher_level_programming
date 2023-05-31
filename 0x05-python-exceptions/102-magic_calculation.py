#!/usr/bin/python3


def magic_calculation(a, b):
    """
    Perform a magic calculation based on the given inputs.

    Args:
        a (int): The first input value.
        b (int): The second input value.

    Returns:
        int: The result of the magic calculation.

    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
