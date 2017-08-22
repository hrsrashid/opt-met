import unittest
from math import exp
from optmet.function import Domain, Function


class TestDomain(unittest.TestCase):
    def setUp(self):
        self.domain = Domain(1, 5)

    def test_contains(self):
        self.assertIn(1, self.domain, 'left bound')
        self.assertIn(3.5, self.domain, 'inside')
        self.assertIn(5, self.domain, 'right bound')
        self.assertNotIn(6, self.domain, 'after')
        self.assertNotIn(-3, self.domain, 'behind')

    def test_length(self):
        self.assertEqual(abs(self.domain), 4)
        self.assertEqual(abs(Domain(0, 0)), 0)

    def test_median(self):
        self.assertEqual(self.domain.median(), 3)


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.eps = 1e-3
        self.places = 2
        self.parabola = Function(f=lambda x: x * x)
        self.func_xy = Function(f=lambda x, y: x * y)

    def test_derivative(self):
        self.assertAlmostEqual(self.parabola.derivative(
            0, epsilon=self.eps),  0, self.places, 'parabola at 0')
        self.assertAlmostEqual(self.parabola.derivative(
            -5, epsilon=self.eps), -10, self.places, 'parabola at -5')
        exponent = Function(f=exp, nargs=1)
        self.assertAlmostEqual(exponent.derivative(
            0, epsilon=self.eps), 1, self.places, 'exponent at 0')
        self.assertAlmostEqual(exponent.derivative(
            10, epsilon=self.eps), 22026.4657948, self.places, 'exponent at 10')

    def test_gradient(self):
        x, y = self.func_xy.gradient(1, 2, epsilon=self.eps)
        self.assertAlmostEqual(x, 2, self.places, 'x')
        self.assertAlmostEqual(y, 1, self.places, 'y')

    def test_derivative2(self):
        self.assertAlmostEqual(self.parabola.derivative2(
            0, epsilon=self.eps), 2, self.places, 'parabola at 0')
        self.assertAlmostEqual(self.parabola.derivative2(
            40, epsilon=self.eps), 2, self.places, 'parabola at 40')

        self.assertAlmostEqual(Function(f=lambda x, y: x + y).derivative2(
            5, 3, epsilon=self.eps, index2=1), 0, self.places, 'x+y by x by y')

        self.assertAlmostEqual(Function(f=lambda x, y: x * y * y).derivative2(
            5, 3, epsilon=self.eps, index2=1), 6, self.places, 'xyy by x by y')

        self.assertAlmostEqual(self.func_xy.derivative2(
            -4, 5, epsilon=self.eps), 0, self.places, 'xy by x by x')
        self.assertAlmostEqual(self.func_xy.derivative2(
            -2, 6, epsilon=self.eps, index2=1), 1, self.places, 'xy by x by y')
