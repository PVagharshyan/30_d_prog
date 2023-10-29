import utility
from studens import Student
from info import Info
from abc import ABC, abstractmethod

class CourseType(ABC):
    @abstractmethod
    def course_type_name(self):
        pass

class UndergraduateCourse(CourseType):
    def course_type_name(self):
        return "Undergraduate Course"

class GraduateCourse(CourseType):
    def course_type_name(self):
        return "Graduate Course"

class Course:
    def __init__(self, name, instructor, content, course_type):
        self.name = name
        self.instructor = instructor
        self.content = content
        self.course_type = course_type
        self._student = []

    def enroll(self, student):
        if not isinstance(student, Student):
            raise ValueError("...")
        self._student.append(student)

    def __str__(self):
        student = ""
        for i in self._student:
            student += str(i) + "\n"
        return f"name: {self.name}, instructor: {self.instructor}, content: {self.content},\nstudents:\n{student}\ntype: {self.course_type.course_type_name()}"

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.check_str_data
    def name(self, value):
        self._name = value

    @property
    def instructor(self):
        return self._instructor

    @instructor.setter
    @utility.check_str_data
    def instructor(self, value):
        self._instructor = value

    @property
    def content(self):
        return self._content

    @content.setter
    @utility.check_str_data
    def content(self, value):
        self._content = value

    @property
    def course(self):
        return str(self.course_type.course_type_name())

    @course.setter
    def course(self, value: CourseType):
        if not isinstance(value, CourseType):
            raise ValueError("...")
        self._cource_type = value

def main():
    i = Info("077858584", "dads", "afd.sdfs@sfs.fsd")
    s1 = Student("poxos", i)
    s2 = Student("esimov", i)
    s3 = Student("petros", i)
    type_c = UndergraduateCourse()
    c = Course("poxos", "petros", "shat lav course", type_c)
    c.enroll(s1)
    c.enroll(s2)
    c.enroll(s3)
    print(c)

if __name__ == "__main__":
    main()
