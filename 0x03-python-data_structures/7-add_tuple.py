#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # pad the tuples with zeros if they are smaller than 2 elements
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # add the elements of the tuples and return a new tuple with the sum
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
