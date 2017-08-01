import unittest
from minimum_golden import find_minimum_golden
from function import Function, Domain


class MinimumGoldenTest(unittest.TestCase):
    def setUp(self):
        self.eps = .001
        self.places = 2

    def test_finds_inside(self):
        self.assertAlmostEqual(find_minimum_golden(
            Function(f=lambda x: x * x, domain=Domain(-2, 3)), self.eps), 0, self.places)

    def test_finds_left_bound(self):
        self.assertAlmostEqual(find_minimum_golden(
            Function(f=lambda x: x * x, domain=Domain(0, 1)), self.eps), 0, self.places)

    def test_finds_right_bound(self):
        self.assertAlmostEqual(find_minimum_golden(
            Function(f=lambda x: x * x, domain=Domain(-1, 0)), self.eps), 0, self.places)
