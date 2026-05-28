from app.models.student import Student


def test_student_creation():
    student = Student(1, "Prateek", 24, "A")

    assert student.person_id == 1
    assert student.name == "Prateek"
    assert student.age == 24
    assert student.grade == "A"


def test_student_role():
    student = Student(1, "Prateek", 24, "A")

    assert student.get_role() == "Student"


def test_student_study():
    student = Student(1, "Prateek", 24, "A")

    assert student.study() == "Prateek is studying"