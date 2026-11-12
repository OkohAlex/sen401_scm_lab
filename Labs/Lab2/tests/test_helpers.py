"""Tests for student score helper functions."""

import unittest

from students import Student
from utils.helpers import get_highest_score, get_lowest_score, get_median_score


class StudentScoreHelperTests(unittest.TestCase):
    def test_empty_cohort_has_no_extrema_or_median(self) -> None:
        self.assertIsNone(get_highest_score([]))
        self.assertIsNone(get_lowest_score([]))
        self.assertIsNone(get_median_score([]))

    def test_extrema_and_median_for_even_cohort(self) -> None:
        students = [
            Student(name="A", score=60),
            Student(name="B", score=80),
            Student(name="C", score=100),
            Student(name="D", score=70),
        ]

        self.assertEqual(get_highest_score(students), students[2])
        self.assertEqual(get_lowest_score(students), students[0])
        self.assertEqual(get_median_score(students), 75.0)


if __name__ == "__main__":
    unittest.main()
