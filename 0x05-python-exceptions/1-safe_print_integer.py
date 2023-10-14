#!/usr/bin/python3
"""this function """


def safe_print_integer(value):
    """this is quite new"""
    try:
        x = int(value)
        print("{}".format(x))
    except ValueError:
        return False
    return True
