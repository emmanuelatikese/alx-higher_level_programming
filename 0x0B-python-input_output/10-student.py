#!/usr/bin/python3
"""this is a class"""


class Student:
    """this class is about to initializ"""
    def __init__(self, first_name, last_name, age):
        """this is where it all begins"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """this is another funtion"""
    def to_json(self, attrs=None):
        """this does something similar"""
        if isinstance(attrs, (list, str)) and attrs is not None:
            new_dict = {}
            for x in attrs:
                if self.__dict__.get(x):
                    new_dict[x] = self.__dict__.get(x)
            return new_dict
        return self.__dict__
