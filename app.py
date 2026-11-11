"""Run a small student-score demonstration using the helper module."""

from students import STUDENTS
from utils.helpers import get_highest_score, get_lowest_score


def main() -> None:
    """Display the sample students and their highest and lowest scores."""
    print("SEN 401 Student Score Demo")
    print("=========================")

    if not STUDENTS:
        print("No student records are available.")
        return

    for student in STUDENTS:
        print(f"{student['name']}: {student['score']:.1f}")

    highest = get_highest_score(STUDENTS)
    lowest = get_lowest_score(STUDENTS)
    if highest is not None and lowest is not None:
        print(f"\nHighest score: {highest['name']} ({highest['score']:.1f})")
        print(f"Lowest score:  {lowest['name']} ({lowest['score']:.1f})")


if __name__ == "__main__":
    main()
