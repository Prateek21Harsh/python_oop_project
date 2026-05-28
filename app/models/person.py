from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id: int, name: str, age: int):
        self._person_id = person_id
        self._name = name
        self._age = age

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def get_role(self):
        pass

    def display_info(self):
        return (
            f"ID: {self.person_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Role: {self.get_role()}"
        )