#!/usr/bin/python3

"""this function has two attributes"""


class Rectangle:
    """this is comment"""

    def __init__(self, width=0, height=0):
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    """ another function called width"""
    @property
    def width(self): return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self): return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self): return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height)*2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        new_list = []
        for x in range(self.__height):
            for y in range(self.__width):
                new_list.append("#")
            if x != self.__height - 1:
                new_list.append("\n")
        return "".join(new_list)
