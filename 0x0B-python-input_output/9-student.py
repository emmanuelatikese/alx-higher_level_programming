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
    def to_json(self):
        """this does something similar"""
        return self.__dict__
