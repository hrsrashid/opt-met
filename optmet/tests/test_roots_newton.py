import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.roots_newton import roots_newton


class RootsNewtonTest(unittest.TestCase):
    def test_linear(self):
        funcs = [
            Function(f=lambda x, y: x + y - 2),
            Function(f=lambda x, y: x - y)
        ]
        self.assertAlmostEqual(roots_newton(funcs), Vector(1, 1), 2)

    def test_non_linear(self):
        funcs = [
            Function(f=lambda x, y: x * x + y - 2),
            Function(f=lambda x, y: x - y)
        ]
        self.assertAlmostEqual(roots_newton(funcs), Vector(-2, -2), 2)
