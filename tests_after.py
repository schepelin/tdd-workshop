import unittest
from solution_after import is_perfect


class TestIsPerfect(unittest.TestCase):

    perfects = [6, 28, 496, 8128, 3355033610]

    def test_perfection(self):
        for n in self.perfects:
            self.assertTrue(is_perfect(n))

    def test_inperfetion(self):
        for x in range(2, 10000):
            if x in self.perfects:
                self.assertTrue(is_perfect(x))
            else:
                self.assertFalse(is_perfect(x))


if __name__ == '__main__':
    unittest.main()
