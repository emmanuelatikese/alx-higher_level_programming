#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    total = 0
    m = 0
    for i in my_list:
        total = total + i[0]*i[1]
        m = m + i[1]
    ans = total / m
    return ans
