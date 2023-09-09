#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    for x in my_list:
        result = result if x < result else x
    return result
