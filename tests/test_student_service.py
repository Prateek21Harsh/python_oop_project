from app.models.student import Student
from app.services.student_service import StudentService



def test_add_student():
    service = StudentService()

    student = Student(1, "Prateek", 24, "A")

    service.add_student(student)

    assert len(service.students) == 1



def test_get_student_by_id():
    service = StudentService()

    student = Student(1, "Prateek", 24, "A")

    service.add_student(student)

    result = service.get_student_by_id(1)

    assert result == student



def test_remove_student():
    service = StudentService()

    student = Student(1, "Prateek", 24, "A")

    service.add_student(student)

    removed = service.remove_student(1)

    assert removed is True
    assert len(service.students) == 0