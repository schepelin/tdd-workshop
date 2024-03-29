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

    def test__add_factor(self):
        classifier = PerfectNumberClassifier(6)
        classifier.add_factor(2)
        classifier.add_factor(3)
        self.assertEqual(classifier.factors, {1, 2, 3, 6})

    def test__calculate_factors_for_6(self):
        expected = {1, 2, 3, 6}
        classifier = PerfectNumberClassifier(6)
        classifier.calculate_factors()
        self.assertEqual(classifier.factors, expected)

    def test__is_prime(self):
        classifier = PerfectNumberClassifier(6)
        self.assertEqual(classifier.is_perfect(), True)


if __name__ == '__main__':
    unittest.main()
