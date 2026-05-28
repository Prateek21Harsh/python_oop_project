from app.models.student import Student
from app.models.teacher import Teacher
from app.services.student_service import StudentService


def main():
    student_service = StudentService()

    student_1 = Student(1, "Prateek", 24, "A")
    student_2 = Student(2, "Rahul", 22, "B")

    teacher = Teacher(101, "Sharma Sir", 40, "Mathematics")

    student_service.add_student(student_1)
    student_service.add_student(student_2)

    print("\n--- Students ---")

    for student in student_service.get_all_students():
        print(student.display_info())
        print(student.study())

    print("\n--- Teacher ---")
    print(teacher.display_info())
    print(teacher.teach())


if __name__ == "__main__":
    main()