import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.minimum_lagrange import find_minimum_lagrange


class MinimumLagrangeTest(unittest.TestCase):
    def test_task_5_1(self):
        func = Function(f=lambda x, y: 2 * x**2 + 5 * y**2 +
                        x * y + x, constraint=lambda x, y: x + .5 * y - 5)
        self.assertAlmostEqual(find_minimum_lagrange(
            func, .5), Vector(4.73, 0.55), 2)

    def test_task_5_2(self):
        func = Function(f=lambda x, y: x**2 + 8 * y**2 + x *
                        y + x, constraint=lambda x, y: 3 * x + y - 2)
        self.assertAlmostEqual(find_minimum_lagrange(
            func, .5), Vector(93 / 140, 1 / 140), 2)
