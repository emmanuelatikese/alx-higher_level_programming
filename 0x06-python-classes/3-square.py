#!/usr/bin/python3
""" same old class but new function area was added """


class Square:
    """check on the class"""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """this just square the size of the function that all"""

    def area(self):
        """this area function got all some on it hand"""
        return (self.__size**2)
