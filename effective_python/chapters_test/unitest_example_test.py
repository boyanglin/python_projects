from unittest import TestCase
from chapters.unitest_example import Solver


class TestSolver(TestCase):
    def test_negative_discr(self):
        s = Solver()
        self.assertRaises(Exception, s.demo, 2, 1, 2)

    def test_demo(self):
        self.fail()

