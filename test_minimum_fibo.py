import unittest
from minimum_fibo import find_minimum_fibo, fiboUntil
from function import Function, Domain


class MinimumFiboTest(unittest.TestCase):
    def setUp(self):
        self.eps = .001
        self.places = 2

    def test_finds_inside(self):
        self.assertAlmostEqual(find_minimum_fibo(
            Function(f=lambda x: x * x, domain=Domain(-2, 3)), self.eps), 0, self.places)

    def test_finds_left_bound(self):
        self.assertAlmostEqual(find_minimum_fibo(
            Function(f=lambda x: x * x, domain=Domain(0, 1)), self.eps), 0, self.places)

    def test_finds_right_bound(self):
        self.assertAlmostEqual(find_minimum_fibo(
            Function(f=lambda x: x * x, domain=Domain(-1, 0)), self.eps), 0, self.places)


class FiboSeqTest(unittest.TestCase):
    def test_gen_fibo_seq(self):
        self.assertSequenceEqual(fiboUntil(5), [1, 1, 2, 3, 5], 'until 5')
        self.assertSequenceEqual(fiboUntil(0), [], 'until 0')
        self.assertSequenceEqual(fiboUntil(1), [1, 1], 'until 1')
        self.assertSequenceEqual(fiboUntil(2), [1, 1, 2], 'until 2')
