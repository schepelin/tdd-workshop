import unittest
from solution_before import PerfectNumberClassifier


class TestIsPerfect(unittest.TestCase):

    def test_is_factor__one_is_always_factor(self):
        classifier = PerfectNumberClassifier(10)
        self.assertTrue(classifier.is_factor(1))

    def test_is_factor__multiple_numbers(self):
        classifier = PerfectNumberClassifier(25)
        self.assertTrue(classifier.is_factor(5))

    def test_is_factor__negative_case(self):
        classifier = PerfectNumberClassifier(7)
        self.assertFalse(classifier.is_factor(3))

    def test__get_factor_for_6(self):
        expected = [1, 2, 3, 6]
        classifier = PerfectNumberClassifier(6)
        self.assertEqual(classifier.get_factors(), expected)


if __name__ == '__main__':
    unittest.main()
