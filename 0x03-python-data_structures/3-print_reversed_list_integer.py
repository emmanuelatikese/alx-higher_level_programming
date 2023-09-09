#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return
    for x in range(len(my_list) - 1, -1, -1):
        if isinstance(my_list[x], int):
            print("{:d}".format(my_list[x]))
    return
