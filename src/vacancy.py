from typing import Any

from src.abstract_class import VacancyABC


class Vacancy(VacancyABC):
    """Класс вакансий. Здесь атрибуты проходят фильтрации, проверки, передаются в функции utils.py, json_saver.py"""

    name: str
    alternate_url: str
    salary: int
    requirement: str
    responsibility: str
    schedule: str

    __slots__ = (
        "name",
        "alternate_url",
        "salary",  # Магический метод для коррекции входящих атрибутов.
        "requirement",  # Только с такими ключами будут приняты
        "responsibility",
        "schedule",
    )

    def __init__(
        self,
        name: str,
        alternate_url: str,
        salary: int,
        requirement: str,
        responsibility: str,
        schedule: str,
    ):
        """Инициализация объектов класса"""
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self._validation_salary(salary)
        self.requirement = self.__validation_requirement(requirement)
        self.responsibility = responsibility  # snippet
        self.schedule = schedule  # schedule - name

    def __str__(self):
        """Str"""
        return (
            f"Вакансия: {self.name}\n"
            f"Ссылка: {self.alternate_url}\n"
            f"Зарплата: {self.salary}\n"
            f"Требования: {self.requirement}\n"
            f"Ответственность: {self.responsibility}\n"
            f"График: {self.schedule}\n"
        )

    def __repr__(self):
        """Repr"""
        return (
            f"Вакансия: {self.name}\n"
            f"Ссылка: {self.alternate_url}\n"
            f"Зарплата: {self.salary}\n"
            f"Требования: {self.requirement}\n"
            f"Ответственность: {self.responsibility}\n"
            f"График: {self.schedule}\n"
        )

    @staticmethod
    def __validation_salary(salary: Any) -> str:
        """Метод валидации атрибута"""
        if salary:
            return salary
        return "Не указана"

    @staticmethod
    def __validation_requirement(requirement: Any) -> str:
        """Метод валидации атрибута"""
        if requirement:
            return requirement
        return "Не указаны"

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list[dict[str, str | int]]:
        """Большая функция для фильтрации данных"""
        new_list = []
        for vacancy in vacancies:
            name = vacancy.get("name")
            alternate_url = vacancy.get("alternate_url")
            if vacancy.get("snippet").get("requirement") is None:
                requirement = "Не указаны"
            else:
                requirement = vacancy.get("snippet").get("requirement")

            if (
                vacancy.get("salary") is None
                or vacancy.get("salary").get("from") is None
            ):
                salary = 0
            else:
                salary = vacancy.get("salary").get("from")

            if vacancy.get("snippet").get("responsibility") is None:
                responsibility = "Не указано"
            else:
                responsibility = vacancy.get("snippet").get("responsibility")

            if vacancy.get("schedule") is None:
                schedule = "Не указано"
            else:
                schedule = vacancy.get("schedule").get("name")

            dict_vac = {
                "name": name,
                "alternate_url": alternate_url,
                "salary": salary,
                "requirement": requirement,
                "responsibility": responsibility,
                "schedule": schedule,
            }
            new_list.append(dict_vac)
        return new_list

    @classmethod
    def __isinstance_data(cls, other: Any) -> int:
        """Проверка на то, что принимаемая переменная в там же классе"""
        if not isinstance(other, Vacancy):
            raise TypeError("Операнд справа должен быть экземпляром класса Vacancy")
        else:
            return other.salary

    # Магические методы сравнения

    def __eq__(self, other):
        sal_1 = self.__isinstance_data(other)
        return self.salary == sal_1

    def __lt__(self, other):
        sal_2 = self.__isinstance_data(other)
        return self.salary < sal_2

    def __le__(self, other):
        sal_3 = self.__isinstance_data(other)
        return self.salary <= sal_3

    def to_dict(self) -> dict[str, str | int]:
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary": self.salary,
            "requirement": self.requirement,
        }
