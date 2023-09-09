#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        return
    count = 0
    for x in matrix:
        for y in x:
            if count < 2:
                print("{} ".format(y), end="")
                count += 1
            else:
                count = 0
                print("{}".format(y))
    return
