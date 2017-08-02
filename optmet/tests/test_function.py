import unittest
from optmet.function import Domain


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
