import requests
from abc import ABC, abstractmethod
from requests import RequestException


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword):
        pass

    # @abstractmethod
    # def __connect(self):
    #     pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    @property
    def vacancies(self):
        return self.__vacancies

    def __connect(self):
        try:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                return response
            else:
                raise RequestException
        except Exception as e:
            print(e)

    def load_vacancies(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 5:
            response = self.__connect()
            vacancies = response.json()['items']
            self.__vacancies.extend(vacancies)
            self.__params['page'] += 1
        return self.__vacancies
            # with open("../data/data.json", "w") as f:
            #     json.dump(vacancies, f)


if __name__ == "__main__":
    api = HeadHunterAPI()
    api.load_vacancies("Python")
    vacans = api.vacancies
    print(vacans[0])