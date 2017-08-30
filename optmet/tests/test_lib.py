import unittest
from optmet.lib import hessian_matrix, jacobian_matrix, mxsum
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


class JacobianMatrixTest(unittest.TestCase):
    def test_matrix(self):
        funcs = [Function(f=lambda x, y: x * y * y),
                 Function(f=lambda x, y: x + y)]
        point = (1, 2)
        expected = [[4, 4], [1, 1]]
        actual = jacobian_matrix(funcs, point)
        assertAlmostEqualMatrices(self, actual, expected, 2)


class MatrixTest(unittest.TestCase):
    def test_sum(self):
        matrices = [[[1, 2], [3, 4]], [[-1, 1], [5, 0]]]
        expected = [[0, 3], [8, 4]]
        actual = mxsum(*matrices)
        assertAlmostEqualMatrices(self, actual, expected, 1)
