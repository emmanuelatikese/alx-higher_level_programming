#!/usr/bin/python
def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(map(lambda x: (x**2), i)), matrix))
