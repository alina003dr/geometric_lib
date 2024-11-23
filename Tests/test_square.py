import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        side = 1
        result = area(side)
        self.assertEqual(result, 1)

    def test_area_zero(self):
        side = 0
        result = area(side)
        self.assertEqual(result, 0)

    def test_perimeter(self):
        side = 1
        result = perimeter(side)
        self.assertEqual(result, 4)

    def test_perimeter_zero(self):
        side = 0
        result = perimeter(side)
        self.assertEqual(result, 0)

    def test_area_neg(self):
        side = -1
        with self.assertRaises(AssertionError):
            area(side)

    def test_perimeter_neg(self):
        side = -1
        with self.assertRaises(AssertionError):
            perimeter(side)


if __name__ == '__main__':
    unittest.main()
