#!/usr/bin/python3

"""this function has two attributes"""


class Rectangle:
    """this is comment"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """this initialize everything"""
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
        Rectangle.number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TyperError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        new_list = []
        for x in range(self.__height):
            for y in range(self.__width):
                new_list.append(str(self.print_symbol))
            if x != self.__height - 1:
                new_list.append("\n")
        return "".join(new_list)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        """this is some comment"""
        return cls(size, size)
