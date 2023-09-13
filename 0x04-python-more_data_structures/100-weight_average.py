#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is []:
        return 0
    n1 = 0
    n2 = 0
    for x in my_list:
        n1 += x[0]*x[1]
        n2 += x[1]
    return n1/n2
