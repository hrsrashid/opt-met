import unittest
from optmet.lib import hessian_matrix, roots_gauss
from optmet.function import Function
from optmet.tests.testutil import assertAlmostEqualMatrices


class HessianMatrixTest(unittest.TestCase):
    def setUp(self):
        self.eps = 1e-3
        self.places = 2

    def test_matrix(self):
        func = Function(f=lambda x, y: x * y * y)
        point = (1, 2)
        expected = [[0, 4], [4, 2]]
        actual = hessian_matrix(func, point, self.eps)
        assertAlmostEqualMatrices(self, actual, expected, self.places)


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
