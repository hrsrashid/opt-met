import unittest
from minimum_dichotomy import find_minimum_dichotomy
from function import Function, Domain


class MinimumDichotomyTest(unittest.TestCase):
    def setUp(self):
        self.eps = .01
        self.delt = .001
        self.places = 2

    def test_finds_inside(self):
        self.assertAlmostEqual(find_minimum_dichotomy(
            Function(f=lambda x: x * x, domain=Domain(-2, 3)), self.eps, self.delt), 0, self.places)

    def test_finds_left_bound(self):
        self.assertAlmostEqual(find_minimum_dichotomy(
            Function(f=lambda x: x * x, domain=Domain(0, 1)), self.eps, self.delt), 0, self.places)

    def test_finds_right_bound(self):
        self.assertAlmostEqual(find_minimum_dichotomy(
            Function(f=lambda x: x * x, domain=Domain(-1, 0)), self.eps, self.delt), 0, self.places)
