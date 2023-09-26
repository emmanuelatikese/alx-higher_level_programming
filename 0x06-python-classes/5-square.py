#!/usr/bin/python3
"""same old function but new things happening"""


class Square:
    """initializing for sure"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    """same old function you know it already"""
    def area(self): return (self._Square__size)**2

    """same old nothing new"""
    @property
    def size(self): return self._Square__size

    """do you need comment so badly"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    """something new but not that new you know print don't you"""
    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            result = ""
            for i in range(self._Square__size):
                result += "#"
            for i in range(self._Square__size):
                print(result)
