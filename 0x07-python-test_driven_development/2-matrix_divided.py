#!/usr/bin/python3
"""A module that divides elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list): A list of lists representing the matrix of integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a matrix (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div and round to 2 decimal places
    divided_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return divided_matrix
