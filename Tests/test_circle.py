import unittest
import math

from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        radius = 1
        result = area(radius)
        self.assertEqual(result, math.pi)

    def test_area_zero(self):
        radius = 0
        result = area(radius)
        self.assertEqual(result, 0)

    def test_perimeter(self):
        radius = 1
        result = perimeter(radius)
        self.assertEqual(result, 2 * math.pi)

    def test_perimeter_zero(self):
        radius = 0
        result = perimeter(radius)
        self.assertEqual(result, 0)

    def test_area_neg(self):
        radius = -1
        with self.assertRaises(AssertionError):
            area(radius)

    def test_perimeter_neg(self):
        radius = -1
        with self.assertRaises(AssertionError):
            perimeter(radius)


if __name__ == '__main__':
    unittest.main()
