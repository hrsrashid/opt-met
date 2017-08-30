import unittest
from optmet.roots_gauss import roots_gauss


class RootsGaussTest(unittest.TestCase):
    def test_simple(self):
        matrix = [[1, 0, 1], [0, 1, 1]]
        x, y = roots_gauss(matrix)
        self.assertAlmostEqual(x, 1, 2, 'x')
        self.assertAlmostEqual(y, 1, 2, 'y')

    def test_singular(self):
        matrix = [[1, 2, 3], [0, 0, 0]]
        with self.assertRaises(Exception):
            roots_gauss(matrix)
