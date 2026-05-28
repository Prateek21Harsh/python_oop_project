from app.models.person import Person


class Student(Person):
    def __init__(self, person_id: int, name: str, age: int, grade: str):
        super().__init__(person_id, name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    def get_role(self):
        return "Student"

    def study(self):
        return f"{self.name} is studying"