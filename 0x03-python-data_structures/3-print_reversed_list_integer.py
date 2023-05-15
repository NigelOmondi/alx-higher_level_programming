#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        reversed_list = reversed(my_list)
        integer_strings = ["{:d}".format(i) for i in reversed_list]
        print("\n".join(integer_strings))
