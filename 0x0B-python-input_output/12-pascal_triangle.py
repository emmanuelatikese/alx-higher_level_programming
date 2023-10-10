#!/usr/bin/python3
"""this is another function"""


def pascal_triangle(n):
    """this function is working quite well"""
    if n <= 0:
        return []
    new_list = []
    c = n + 1
    for x in range(1, c):
        r, a = [], 1
        for y in range(1, x + 1):
            r.append(a)
            a *= (x - y) // y
        new_list.append(r)
    return new_list
