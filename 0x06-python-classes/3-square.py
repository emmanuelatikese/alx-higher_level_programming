#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size
    def area(self):
        return pow(self.size, 2)
    @size.property
    def size(self):
        return self.size
    @size.setter
    def size(self, value):
        if isinstance(self.size, int) == False:
            raise TypeError("size must be an integer")
        elif self.size < 0:
           raise ValueError("size must be >= 0")
        self.size = value 
