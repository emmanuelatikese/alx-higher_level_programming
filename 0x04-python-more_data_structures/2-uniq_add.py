#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    result = 0
    for x in my_list:
        if x in uniq:
            continue
        else:
            uniq.append(x)
            result += x
    return result
