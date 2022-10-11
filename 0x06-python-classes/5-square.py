#!/usr/bin/python3
"""Square is a class"""

class Square:
    """Square has attributes"""

    def __init__(self, size=0):
        self.size = size
    def area(self):
        """Area is a function within the class"""

        return pow(self.size, 2)
    @size.property
    def size(self):
        """This is to retrieve the original value"""

        return self.size
    @size.setter
    def size(self, value):
        """This is help set the size to value"""

        if isinstance(self.size, int) == False:
            raise TypeError("size must be an integer")
        elif self.size < 0:
           raise ValueError("size must be >= 0")
        self.size = value 
    def my_print(self):
        """To enable printing"""

        if self.size == 0:
            print("")
        for a in range(self.size):
            for b in range(self.size):
                print("#", end='')
                print('')
