#!/usr/bin/python3
"""returns boolean base on a condition"""


def inherits_from(obj, a_class):
    """returns true or false"""
    return True if isinstance(obj, a_class) else False
