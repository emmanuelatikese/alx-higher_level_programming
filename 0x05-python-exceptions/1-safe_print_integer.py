#!/usr/bin/python3
"""this function """


def safe_print_integer(value):
    """this is quite new"""
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        return False
    return True
