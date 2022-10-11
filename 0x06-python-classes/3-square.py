#!/usr/bin/python3
"""Square is a class"""

class Square:
    """Square has attributes"""

    def __init__(self, size=0):
        """ The class is then initialize"""

        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
    def area(self):
        """Area is a function """

        return pow(self.size, 2)
