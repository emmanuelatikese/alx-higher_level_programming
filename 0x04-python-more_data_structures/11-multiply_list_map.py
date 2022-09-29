#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    a = lambda x: x*4
    return list(map(a, my_list))
