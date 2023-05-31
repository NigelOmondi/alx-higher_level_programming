#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers from a list.

    Args:
        my_list (list, optional): The list to print. Defaults to an empty list.
        x (int, optional): The number of integers to print. Defaults to 0.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end='')
                count += 1
    except IndexError:
        pass
    print()
    return count
