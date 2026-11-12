"""Utilities for calculating statistics from student records."""

from typing import Optional, TypedDict


class Student(TypedDict):
    """A student record containing a name and a score."""

    name: str
    score: float


def get_highest_score(students: list[Student]) -> Optional[Student]:
    """Return the student with the highest score, or None for an empty list."""
    if not students:
        return None
    return max(students, key=lambda student: student["score"])


def get_lowest_score(students: list[Student]) -> Optional[Student]:
    """Return the student with the lowest score, or None for an empty list."""
    if not students:
        return None
    return min(students, key=lambda student: student["score"])
