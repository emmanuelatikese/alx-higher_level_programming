#!/usr/bin/python3
"""same old function but new features"""


class Square:
    """this is where the function get started"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    """same old area function for sure"""
    def area(self): return (self._Square__size)**2

    """this is a size function it get a getter funcdtion"""
    @property
    def size(self): return self._Square__size

    """this is a setter for sure with all decorator in there"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
