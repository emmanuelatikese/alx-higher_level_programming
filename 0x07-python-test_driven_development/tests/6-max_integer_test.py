#!/usr/bin/python3
"""this is testing """

import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_Max(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_notinteger(self):
        self.assertEqual(TypeError, max_integer, True)
