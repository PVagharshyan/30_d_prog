from typing import List
from person import Person
import copy
import utility

class Course:
    ...

class Student(Person):
    def __init__(self, name: str, contact_info: str):
        super().__init__(name, contact_info)
        self._courses: List[Course] = []

    @property
    def cources(self):
        return self._courses

    @cources.setter
    @utility.container_type_checking(list, Course)
    def courses(self, value: List[Course]):
        self._courses = copy.deepcopy(value)

    @utility.type_checking(Course)
    def enroll(self, course: "Course") -> None:
        self.courses.append(course)

    def view_progress(self) -> None:
        for course in self.courses:
            print(f"{self.name} is enrolled in {course.name}")
