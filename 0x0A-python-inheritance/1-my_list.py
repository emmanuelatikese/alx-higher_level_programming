#!/usr/bin/python3
"""this class inherit list"""


class MyList(list):
    """this class begins"""

    def __init__(self):
        """this initialize the list class"""
        super().__init__()

    def print_sorted(self):
        """return print sorted list"""
        return print(sorted(self))
