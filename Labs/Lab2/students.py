"""Validated student records used by the SEN 401 demonstration application."""

from pydantic import BaseModel, ConfigDict, Field


class Student(BaseModel):
    """A student name and an examination score from 0 to 100."""

    model_config = ConfigDict(str_strip_whitespace=True)

    name: str = Field(min_length=1, description="Student's name")
    score: float = Field(ge=0, le=100, description="Examination score")


STUDENTS = [
    Student(name="Tola", score=78.0),
    Student(name="Zainab", score=91.5),
    Student(name="Emeka", score=84.0),
    Student(name="Kemi", score=69.5),
]
