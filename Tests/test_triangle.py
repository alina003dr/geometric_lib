import unittest
from triangle import perimeter, area


class TestTriangle(unittest.TestCase):
    def test_area(self):
        a, b, c = 3, 4, 5
        result = area(a, b, c)
        self.assertEqual(result, 6)

    def test_perimeter(self):
        a, b, c = 2, 3, 4
        result = perimeter(a, b, c)
        self.assertEqual(result, 9)

    def test_area_neg(self):
        a, b, c = -5, -12, -13
        with self.assertRaises(AssertionError):
            area(x, y, z)

    def test_perimeter_neg(self):
        a, b, c = -5, -12, -13
        with self.assertRaises(AssertionError):
            perimeter(x, y, z)


if __name__ == '__main__':
    unittest.main()
