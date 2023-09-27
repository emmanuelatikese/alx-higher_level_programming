#!/usr/bin/python3
"""same old function but new things happening"""


class Square:
    """initializing for sure"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        if type(position) != tuple and len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.new_pos = position

    """same old function you know it already"""
    def area(self): return (self._Square__size)**2

    """same old nothing new"""
    @property
    def size(self): return self._Square__size

    """do you need comment so badly"""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    """something new but not that new you know print don't you"""
    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            result = ""
            if self.new_pos[0] > 0:
                for y in range(self.new_pos[0]):
                    result += " "
            for i in range(self._Square__size):
                result += "#"
                for i in range(self._Square__size):
                    print(result)

    @property
    def position(self): return self.new_pos

    @position.setter
    def position(self, value):
        if type(value) != tuple and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.new_pos = value
