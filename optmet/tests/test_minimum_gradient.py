import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.minimum_gradient import find_minimum_gradient


class MinimumGradientTest(unittest.TestCase):
    def test_parabola(self):
        parabola = Function(f=lambda x: x * x, x0=Vector(1))
        minimum = find_minimum_gradient(parabola)
        self.assertAlmostEqual(minimum, 0, 2)
