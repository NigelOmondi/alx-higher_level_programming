#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # iterate over each row in the matrix
    for row in matrix:
        # iterate over each integer in the row
        for num in row:
            # print the integer with a width of 5 (adjust as necessary)
            # followed by a space to separate it from the next integer
            print("{:5}".format(num), end="")
        # print a newline after each row is complete
        print()
