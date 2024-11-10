import json
import os
from json import JSONDecodeError
from typing import Any, AnyStr


class JSONSaver:
    """Класс сохранения данных в файл"""

    name: str
    path: str

    def __init__(self, name="data.json") -> None:
        """Метод инициализации. Есть статичный параметр"""
        self.name = name
        self.path = os.path.join(os.path.dirname(__file__), "..", "data", self.name)

    def open_json(self) -> list:
        """Функция открытия файла. В случае ошибки придет уведомление"""
        try:
            with open(self.path) as f:
                return json.load(f)
        except JSONDecodeError:
            return []
        except Exception as e:
            print(e)
            return []

    def add_vacancy(self, vacancy: AnyStr) -> str:
        """Функция добавления вакансии в конец списка файла"""
        vacancy_list = self.open_json()
        new_list = []
        for vacancy_dict in vacancy_list:
            new_list.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url not in new_list:
            vacancy_list.append(vacancy.to_dict())
            with open(self.path, "w") as file:
                json.dump(vacancy_list, file, ensure_ascii=False, indent=4)
        else:
            return "Данная вакансия уже существует"

    def delete_vacancy(self, vacancy: Any) -> str:
        """Функция удаления вакансии из файла"""
        open_json = self.open_json()
        new_list_url = []
        for vacancy_dict in open_json:
            new_list_url.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url in new_list_url:
            for i in range(len(open_json)):
                if open_json[i - 1]["alternate_url"] == vacancy.alternate_url:
                    del open_json[i - 1]
        else:
            return "Вакансия не найдена."

        with open(self.path, "w") as file:
            json.dump(open_json, file, ensure_ascii=False, indent=4)
