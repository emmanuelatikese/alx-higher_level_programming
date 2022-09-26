#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = my_list.copy()
    for i in range(len(my_list) - 1):
        if my_list[i] % 2 == 0:
            a[i] = True
        a[i] = False
    return a
