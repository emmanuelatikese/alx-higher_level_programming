#!/usr/bin/python3
def uniq_add(my_list=[]):
    for x in my_list:
        if my_list.count(x) > 1:
            my_list.remove(x)
    result = 0
    for x in my_list:
        result += x
    return result
