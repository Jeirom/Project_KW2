import json
from src.vacancy import Vacancy

from typing import List, Dict, Any

from src.abs_file_handler import AbstractFileHandler


class JSONFileHandler(AbstractFileHandler):
    """Класс для работы с JSON-файлами"""

    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = filename

    def load_data(self) -> List[Dict[str, Any]]:
        """Метод загрузки файла"""
        try:
            with open(self.__filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data: List[Dict[str, Any]]) -> None:
        """Метод сохранения файла и удаления дубликатов"""
        existing_data = self.load_data()
        existing_data.extend(data)
        unique_data = list({v["url"]: v for v in existing_data}.values())
        with open(self.__filename, "w") as file:
            json.dump(unique_data, file, ensure_ascii=False, indent=4)

    def delete_data(self, criteria: Dict[str, Any]) -> None:
        """Метод удаления данных"""
        data = self.load_data()
        filtered_data = [
            vac for vac in data if not all(vac[k] == v for k, v in criteria.items())
        ]
        with open(self.__filename, "w") as file:
            json.dump(filtered_data, file, indent=4)
