from app.models.person import Person


class Teacher(Person):
    def __init__(self, person_id: int, name: str, age: int, subject: str):
        super().__init__(person_id, name, age)
        self._subject = subject

    @property
    def subject(self):
        return self._subject

    def get_role(self):
        return "Teacher"

    def teach(self):
        return f"{self.name} is teaching {self.subject}"