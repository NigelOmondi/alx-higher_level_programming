#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # initialize an empty list to store the results
    results = []

    # iterate over each element of the input list
    for num in my_list:
        # check if the current element is divisible by 2
        if num % 2 == 0:
            # append True to the results list if it is divisible by 2
            results.append(True)
        else:
            # append False to the results list if it is not divisible by 2
            results.append(False)

    # return the results list
    return results
