#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a < 2:
        if len_a == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)
    elif len_a > 2:
        tuple_a = tuple_a[:2]
    if len_b < 2:
        if len_b == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)
    elif len_b > 2:
        tuple_b = tuple_b[:2]
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
