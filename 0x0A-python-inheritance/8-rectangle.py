#!/usr/bin/python3
"""This is just an empty function"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """this function initialize"""
    def __init__(self, width, height):
        if self.integer_validator("width", width) is None:
            Rectangle.__width = width
        if self.integer_validator("height", height) is None:
            Rectangle.__height = height
