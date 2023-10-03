#!/usr/bin/python3
"""this function deals with matrices"""


def matrix_divided(matrix, div):
    len_list = len(matrix[0])
    for x in matrix:
        if len(x) != len_list:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(y/div, 2) for y in x] for x in matrix]
