#!/usr/bin/python3
"""this function does a lot"""


def add_attribute(ob, name, val):
    if not hasattr(ob, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(ob, name, val)
