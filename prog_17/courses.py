from typing import List
from students import Student, Course as Course_s
from teachers import Teacher, Course as Course_t
import utility

class Course(Course_s, Course_t):
    def __init__(self, name: str):
        self.name: str = name
        self.teacher: Optional[Teacher] = None
        self.students: List[Student] = []
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str) -> None:
        self._name = value

    @utility.container_type_checking(list, Student)
    def enroll_students(self, students: List['Student']) -> None:
        for student in students:
            self.students.append(student)

    def view_enrolled_students(self) -> None:
        print(f"Students enrolled in {self.name}:")
        for student in self.students:
            print(student.name)

class MathCourse(Course):
    def __init__(self, name: str):
        super().__init__(name)

class EnglishCourse(Course):
    def __init__(self, name: str):
        super().__init__(name)
