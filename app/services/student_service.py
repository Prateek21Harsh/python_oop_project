from app.models.student import Student


class StudentService:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)
        return student

    def get_student_by_id(self, student_id: int):
        for student in self.students:
            if student.person_id == student_id:
                return student
        return None

    def get_all_students(self):
        return self.students

    def remove_student(self, student_id: int):
        student = self.get_student_by_id(student_id)

        if student:
            self.students.remove(student)
            return True

        return False