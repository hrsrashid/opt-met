import unittest
from optmet.function import Function
from optmet.minimum_hessian import find_minimum_hessian, hessian_matrix
from optmet.tests.testutil import assertAlmostEqualMatrices


class MinimumHessianTest(unittest.TestCase):
    pass


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
