#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list (list, optional): The list to print. Defaults to an empty list.
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            count += 1
    except IndexError:
        pass
    print()
    return count
