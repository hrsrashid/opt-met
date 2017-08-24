import unittest
from optmet.function import Function
from optmet.vector import Vector
from optmet.minimum_fletcher_reeves import find_minimum_fletcher_reeves


class MinimumFletcherReevesTest(unittest.TestCase):
    def test_parabola(self):
        parabola = Function(f=lambda x: x * x, x0=Vector(1))
        minimum = find_minimum_fletcher_reeves(parabola)
        self.assertAlmostEqual(minimum, 0, 2)

    def test_multivar(self):
        func = Function(f=lambda x, y: x * x + y * y, x0=Vector(1.1, 0.9))
        minimum = find_minimum_fletcher_reeves(func)
        self.assertAlmostEqual(minimum, Vector(0, 0), 2)

    def test_multivar2(self):
        func = Function(f=lambda x, y: 100 * (y - x * x) **
                        2 + (1 - x)**2, x0=Vector(-1.2, 1))
        minimum = find_minimum_fletcher_reeves(func)
        self.assertAlmostEqual(minimum, Vector(1, 1), 2)

    def test_task_func(self):
        func = Function(f=lambda x, y: x * x + 6 * y *
                        y + x * y + x, x0=Vector(1.5, 1.1))
        minimum = find_minimum_fletcher_reeves(func)
        self.assertAlmostEqual(minimum, Vector(-12 / 23, 1 / 23), 2)
