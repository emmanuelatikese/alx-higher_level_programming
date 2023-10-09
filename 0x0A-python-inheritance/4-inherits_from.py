#!/usr/bin/python3
"""returns boolean base on a condition"""


def inherits_from(obj, a_class):
    """returns true or false"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
