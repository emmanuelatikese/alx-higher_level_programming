#!/usr/bin/python3
"""this class is base on the other
class from the previous file
"""


class Square:
    """
this init function do get a lot of things going for sure
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
