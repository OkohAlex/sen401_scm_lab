"""Utilities for calculating statistics from student records."""

from collections.abc import Sequence
from statistics import median

from students import Student


def get_highest_score(students: Sequence[Student]) -> Student | None:
    """Return the student with the highest score, or None for no records."""
    if not students:
        return None
    return max(students, key=lambda student: student.score)


def get_lowest_score(students: Sequence[Student]) -> Student | None:
    """Return the student with the lowest score, or None for no records."""
    if not students:
        return None
    return min(students, key=lambda student: student.score)


def get_median_score(students: Sequence[Student]) -> float | None:
    """Return the median score, or None when there are no records."""
    if not students:
        return None
    return float(median(student.score for student in students))
