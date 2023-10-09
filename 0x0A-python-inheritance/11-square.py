#!/usr/bin/python3
"""This is just an empty function"""
B = __import__("9-rectangle").Rectangle


class Square(B):
    """this function initialize"""
    def __init__(self, size):
        if self.integer_validator("size", size) is None:
            self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return (self.__size)**2
