#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in my_list:
        if my_list.count(i) > 1:
            my_list.remove(i)
    return sum(my_list)
