#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            print("{}".format(matrix[x][i]), end=" ")
