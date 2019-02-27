import unittest

import pytest

from patterner.patterns import Part, Pattern, Point
from patterner.svg import Arc, Line, Path


class TestPoint(unittest.TestCase):
    def test_values(self):
        point = Point(8, 2)
        self.assertEqual(point.x, 8)
        self.assertEqual(point.y, 2)

    def test_subtraction(self):
        value = Point(5, 4) - Point(2, 3)
        self.assertEqual(value, (3, 1))

    def test_subtraction_int(self):
        value = Point(5, 9) - 2
        self.assertEqual(value, (3, 7))

    def test_subtraction_wrong_type(self):
        with pytest.raises(TypeError):
            Point(5, 9) - "wrong"

    def test_addition(self):
        value = Point(5, 4) + Point(2, 3)
        self.assertEqual(value, (7, 7))

    def test_addition_int(self):
        value = Point(5, 9) + 2
        self.assertEqual(value, (7, 11))

    def test_addition_wrong_type(self):
        with pytest.raises(TypeError):
            Point(5, 9) + "wrong"
