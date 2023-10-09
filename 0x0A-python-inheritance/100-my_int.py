#!/usr/bin/python3
"""this function inherit Int"""


class MyInt(int):
    """initialize the function"""
    def __init__(self, n):
        self.n = n

    def __eq__(self, n):
        return False if isinstance(n, int) else True

    def __ne__(self, n):
        return True if isinstance(n, int) else False
