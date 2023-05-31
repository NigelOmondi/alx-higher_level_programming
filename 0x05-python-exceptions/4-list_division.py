#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element from two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        list: A new list with division results.
    """
    result = []
    for i in range(list_length):
        try:
            div = 0
            if i < len(my_list_1) and i < len(my_list_2):
                div = my_list_1[i] / my_list_2[i]
            elif i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result.append(div)
    return result
