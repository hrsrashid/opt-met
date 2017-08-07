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
        self.assertEqual(self.domain.len(), 4)
        self.assertEqual(Domain(0, 0).len(), 0)

    def test_median(self):
        self.assertEqual(self.domain.median(), 3)


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.eps = 1e-3
        self.places = 2

    def test_derivative(self):
        parabola = Function(f=lambda x: x * x)
        self.assertAlmostEqual(parabola.derivative(
            0, epsilon=self.eps),  0, self.places, 'parabola at 0')
        self.assertAlmostEqual(parabola.derivative(
            -5, epsilon=self.eps), -10, self.places, 'parabola at -5')
        exponent = Function(f=exp)
        self.assertAlmostEqual(exponent.derivative(
            0, epsilon=self.eps), 1, self.places, 'exponent at 0')
        self.assertAlmostEqual(exponent.derivative(
            5, epsilon=self.eps / 10), 148.4, 1, 'exponent at 5')

    def test_gradient(self):
        func = Function(f=lambda x, y: x * y)
        x, y = func.gradient(1, 2, epsilon=self.eps)
        self.assertAlmostEqual(x, 2, self.places, 'x')
        self.assertAlmostEqual(y, 1, self.places, 'y')
