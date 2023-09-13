#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    some_list = []
    for x in matrix:
        for y in x:
            some_list.append(y**2)
        new_list.append(some_list)
        some_list = []
    return new_list
