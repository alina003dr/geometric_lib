import unittest
from calculate import calc


class TestCalculate(unittest.TestCase):
    def test_neg_size_area_circle(self):
        fig = 'circle'
        func = 'area'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_area_square(self):
        fig = 'square'
        func = 'area'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_area_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [-5, -12, -13]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_circle(self):
        fig = 'circle'
        func = 'perimeter'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_square(self):
        fig = 'square'
        func = 'perimeter'
        size = [-1]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_neg_size_perimeter_triangle(self):
        fig = 'triangle'
        func = 'perimeter'
        size = [-5, -12, -13]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_wrong_size_triangle(self):
        fig = 'triangle'
        func = 'area'
        size = [1, 2, 10]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)


if __name__ == '__main__':
    unittest.main()
