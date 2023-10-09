#!/usr/bin/python3
"""this functnion return boolean base on whether an obj
is instance of a class"""


def is_same_class(obj, a_class):
    """this returns boolean"""
    return True if type(obj) == a_class else False
