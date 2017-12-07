import unittest
from solution_before import (
    is_factor,
)


class TestIsPerfect(unittest.TestCase):

    def test_is_factor_helper(self):
        self.assertTrue(is_factor(1, 10))
        self.assertFalse(is_factor(2, 3))


if __name__ == '__main__':
    unittest.main()
