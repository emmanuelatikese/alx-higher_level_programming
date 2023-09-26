#!/usr/bin/python3
""" same old class but new function area was added """


class Square:
    """check on the class"""
    def __init__(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    """this just square the size of the function that all"""

    def area(self): return (self._Square__size**2)
