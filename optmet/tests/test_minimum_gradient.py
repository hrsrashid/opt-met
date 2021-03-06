import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.minimum_gradient import find_minimum_gradient


class MinimumGradientTest(unittest.TestCase):
    def test_parabola(self):
        parabola = Function(f=lambda x: x * x, x0=Vector(1))
        minimum = find_minimum_gradient(parabola)
        self.assertAlmostEqual(minimum, 0, 2)

    def test_multivar(self):
        func = Function(f=lambda x, y: x * x + y * y, x0=Vector(1.1, 0.9))
        minimum = find_minimum_gradient(func)
        self.assertAlmostEqual(minimum, Vector(0, 0), 2)
