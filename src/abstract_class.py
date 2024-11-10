from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для класса вакансий"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Запрос get и запись в vacancies инфы по вакансии"""
        pass


class JSONABC(ABC):
    """Родительский класс для Json класса"""

    def open_json(self):
        """Открывает Json файл для дальнейшего считывания и фильтрации"""
        pass

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в уже созданный файл"""
        pass

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из уже созданного файла"""
        pass


class VacancyABC:

    @classmethod
    def cast_to_object_list(cls, vacancies: list):
        """Большая функция для фильтрации данных"""
        pass

    @abstractmethod
    def to_dict(self):
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        pass
