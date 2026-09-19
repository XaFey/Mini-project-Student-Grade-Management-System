from abc import ABC, abstractmethod
import csv
import os

class Gradeable(ABC):
    """Abstract base class for gradeable entities."""
    @abstractmethod
    def calculate_grade(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

class Student(Gradeable):
    def __init__(self, name:str, grades: list[float]):
        """Student class with name and grades."""
        self.name = name
        self.grades = grades

    def calculate_grade(self):
        """Calculate average grade."""
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def to_dict(self):
        """Return student data as dictionary."""
        return {"type": "student", "name": self.name, "grades": ",".join(map(str, self.grades))}

class Course(Gradeable):
    def __init__(self, name: str, student_grades: dict[str, float]):
        """Course class with name and student grades."""
        self.name = name
        self.student_grades = student_grades

    def calculate_grade(self):
        """Calculate average grade."""
        grades = list(self.student_grades.values())
        return sum(grades) / len(grades) if grades else 0.0

    def to_dict(self):
        """Return course data as dictionary."""
        return {"type": "course", "name": self.name, "student_grades": str(self.student_grades)}

