import unittest
from observables import *


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(p4_3_1([[1, -1, ], [-1, 1]]), ([0, 1]))

    def test_2(self):
        self.assertEqual(p4_3_1([[0, -1], [-1, 0]]), ([0, 1]))

    def test_3(self):
        self.assertEqual(p4_3_1([[0, 1], [1, 0]]), ([0, 1]))

    def test_4(self):
        self.assertEqual(p4_3_2([[1, -1], [-1, 1]]), ([0.5, 1]))

    def test_5(self):
        self.assertEqual(p4_3_2([[0, 1], [1, 0]]), ([0.5, 1]))

    def test_6(self):
        self.assertEqual(p4_3_2([[0, -1, ], [-1, 0]]), ([0.5, 1]))

    def test_7(self):
        v1 = [[(2 ** 1 / 2) / 2, (2 ** 1 / 2) / 2], [(2 ** 1 / 2) / 2, -(2 ** 1 / 2) / 2]]
        v2 = [[0, 1], [1, 0]]
        self.assertEqual(p4_4_1(v1, v2), (True))

    def test_8(self):
        m1 = [[0, 1, 1, 0]]
        m2 = [[(2 ** 1 / 2) / 2, (2 ** 1 / 2) / 2], [(2 ** 1 / 2) / 2, -(2 ** 1 / 2) / 2],
              [(2 ** 1 / 2) / 2, (2 ** 1 / 2) / 2], [(2 ** 1 / 2) / 2, -(2 ** 1 / 2) / 2],
              [(2 ** 1 / 2) / 2, (2 ** 1 / 2) / 2], [(2 ** 1 / 2) / 2, -(2 ** 1 / 2) / 2]]
        m = 3
        self.assertEqual(p4_4_2(m1, m2, m), ([0.3, 0.7, 0.5, 0.5]))


if __name__ == '__main__':
    unittest.main()