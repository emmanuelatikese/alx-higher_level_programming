#!/usr/bin/python3
"""Square is a class"""

class Square:
    """Square do have attributes"""

    def __init__(self, size=0):
        """The class is initialize"""

        self.size = size
    def area(self):
        """Area function is within the class"""

        return pow(self.size, 2)
    @size.property
    def size(self):
        """The funtion size is to retrieve the original value"""

        return self.size
    @size.setter
    def size(self, value):
        """This function is a setter"""

        if isinstance(self.size, int) == False:
            raise TypeError("size must be an integer")
        elif self.size < 0:
           raise ValueError("size must be >= 0")
        self.size = value 
