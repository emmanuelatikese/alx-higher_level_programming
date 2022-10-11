#!/usr/bin/python3
"""Square is a class."""

class Square:
    """Square has attributes."""

    def __init__(self, size=0):
        """the class is initialize"""

        if isinstance(size, int) == False:
            self.size = int(size)
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
