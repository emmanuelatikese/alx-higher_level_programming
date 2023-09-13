#!/usr/bin/python
def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(map(lambda x: x*x, i)), matrix))
