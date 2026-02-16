import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_normal(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_zero(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_area_negative(self):
        res = area(-5, 10)
        self.assertEqual(res, -50)