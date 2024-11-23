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

    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and c + b > a


if __name__ == '__main__':
    unittest.main()
