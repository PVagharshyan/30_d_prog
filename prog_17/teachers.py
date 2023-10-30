from typing import List
from person import Person
from students import Student

class Course:
    ...

class Teacher(Person):
    def __init__(self, name: str, contact_info: str, subject_taught: str):
        super().__init__(name, contact_info)
        self.subject_taught: str = subject_taught

    def manage_course(self, course: "Course", students: List[Student]) -> None:
        if not isinstance(students, list) or not isinstance(course, Course):
            raise ValueError("...")
        for i in students:
            if not isinstance(i, Student):
                raise ValueError("...")
        course.teacher = self
        course.enroll_students(students)
