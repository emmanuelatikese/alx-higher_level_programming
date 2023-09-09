#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    result = my_list[0]
    for x in my_list[1:]:
        result = result if x < result else x
    return result
