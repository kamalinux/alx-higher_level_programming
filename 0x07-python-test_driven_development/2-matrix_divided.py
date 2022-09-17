#!/usr/bin/python3
# Author: @kamalinux

"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size
        ZeroDivisionError: If div is zero
    """

    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_msg)

    row_size = 0
    row_msg = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(matrix_msg)

        if row_size != 0 and len(elems) != row_size:
            raise TypeError(row_msg)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(matrix_msg)

        row_size = len(elems)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    re = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (re)
