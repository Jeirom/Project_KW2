from abc import ABC, abstractmethod

class Parser:
    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    @abstractmethod
    def __connect(self):
        pass
