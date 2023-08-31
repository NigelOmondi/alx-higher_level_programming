#!/usr/bin/python3
"""Find the peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """The sorting algorithm that finds peak"""
    if integer_list == []:
        return None

    size = len(integer_list)
    m = int(size / 2)
    intl = integer_list

    if m - 1 < 0 and m + 1 >= size:
        return intl[m]
    elif m - 1 < 0:
        return intl[m] if intl[m] > intl[m + 1] else intl[m + 1]
    elif m + 1 >= size:
        return intl[m] if intl[m] > intl[m - 1] else intl[m - 1]

    if intl[m - 1] < intl[m] > intl[m + 1]:
        return intl[m]
    if intl[m + 1] > li[m - 1]:
        return find_peak(intl[m:])
    return find_peak(li[:m])
