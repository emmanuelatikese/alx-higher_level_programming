#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if len(tuple_a) == 0:
        a = (0, 0)
    elif len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    elif len(tuple_a) > 2:
        a = (tuple_a[0], tuple_a[1])
    if len(tuple_b)  == 0:
        b = (0, 0)
    elif len(tuple_b) == 1:
        b = (tuple_b[0], 0)
    elif len(tuple_b) > 2:
        b = (tuple_b[0], tuple_b[1])
    result1 = a[0] + b[0]
    result2 = a[1] + b[1]
    return (result1, result2)
