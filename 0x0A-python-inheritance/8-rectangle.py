#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""This is just an empty function"""


class Rectangle(BaseGeometry):
    """these are attributes"""
    __width = None
    __height = None

    """this function initialize"""
    def __init__(self, width, height):
        if self.integer_validator("width", width) is None:
            Rectangle.__width = width
        if self.integer_validator("height", height) is None:
            Rectangle.__height = height
