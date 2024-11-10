import json

from json import JSONDecodeError
from src.vacancy import Vacancy
import os
from typing import List, Dict, Any

from src.abs_file_handler import AbstractFileHandler


class JSONSaver:

    def __init__(self, name="data.json"):
        self.name = name
        self.path = os.path.join(os.path.dirname(__file__), "..", "data", self.name)

    def open_json(self):
        try:
            with open(self.path) as f:
                return json.load(f)
        except JSONDecodeError:
            return []
        except Exception as e:
            print(e)
            return []

    def add_vacancy(self, vacancy):
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

    def delete_vacancy(self, vacancy):
        open_json = self.open_json()
        new_list_url = []
        for vacancy_dict in open_json:
            new_list_url.append(vacancy_dict.get("alternate_url"))
        if vacancy.alternate_url in new_list_url:
            for i in range(len(open_json)):
                if open_json[i-1]['alternate_url'] == vacancy.alternate_url:
                    del open_json[i-1]
        else:
            return "Вакансия не найдена."

        with open(self.path, "w") as file:
            json.dump(open_json, file, ensure_ascii=False, indent=4)