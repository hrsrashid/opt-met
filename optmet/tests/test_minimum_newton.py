import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.minimum_newton import find_minimum_newton


class MinimumNewtonTest(unittest.TestCase):
    def test_parabola(self):
        parabola = Function(f=lambda x: x * x, x0=Vector(1))
        minimum = find_minimum_newton(parabola)
        self.assertAlmostEqual(minimum, 0, 2)

    def test_multivar(self):
        func = Function(f=lambda x, y: x * x + y * y, x0=Vector(1.1, 0.9))
        minimum = find_minimum_newton(func)
        self.assertAlmostEqual(minimum, Vector(0, 0), 2)

    def test_multivar2(self):
        func = Function(f=lambda x, y: 100 * (y - x * x) **
                        2 + (1 - x)**2, x0=Vector(-1.2, 1))
        minimum = find_minimum_newton(func)
        self.assertAlmostEqual(minimum, Vector(1, 1), 2)
