from person import Person
from courses import Course, MathCourse, EnglishCourse
from students import Student
from teachers import Teacher

if __name__ == "__main__":
    student1 = Student("Alice", "alice@email.com")
    student2 = Student("Bob", "bob@email.com")

    math_course = MathCourse("Math 101")
    english_course = EnglishCourse("English 101")

    teacher = Teacher("Ms. Smith", "teacher@email.com", "Math")

    teacher.manage_course(math_course, [student1, student2])
    teacher.manage_course(english_course, [student1])

    student1.view_progress()
    student2.view_progress()
    math_course.view_enrolled_students()
    english_course.view_enrolled_students()
