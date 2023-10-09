#!/usr/bin/python3
"""This is just an empty function"""


class BaseGeometry:
    """this function not initialize"""
    def integer_validator(self, name, value):
        """this checks value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.value = value
        self.name = name

    def area(self):
        """this raise exception that all"""
        raise Exception("area() is not implemented")
