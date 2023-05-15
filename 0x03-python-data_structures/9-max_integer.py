#!/usr/bin/python3
def max_integer(my_list=[]):
    # check if the list is empty
    if not my_list:
        # return None if the list is empty
        return None

    # set the initial max integer to the first element of the list
    max_num = my_list[0]

    # iterate over the remaining elements of the list
    for num in my_list[1:]:
        # update the max integer if the current element is bigger
        if num > max_num:
            max_num = num

    # return the max integer
    return max_num
