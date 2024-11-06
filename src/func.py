import json
import logging
import os

# Получаем путь к директории src
SRC_DIR = os.path.dirname(os.path.abspath(__file__))

# Получаем путь к корневой директории проекта (на одну директорию выше src)
BASE_DIR = os.path.dirname(SRC_DIR)

# Создаем путь до директории logs в корне проекта
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Проверяем, существует ли директория logs, если нет - создаем
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Указываем путь до файла с логами
log_file = os.path.join(LOG_DIR, "utils_logger")

# Основная конфигурация logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_file,  # Запись логов в файл
    filemode="w",
)  # Перезапись файла при каждом запуске

# Создаем логер для компонентов программы
trans_data_loger = logging.getLogger("trans.data.loger")



def load_json(file_path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о вакансиях."""

    trans_data_loger.info(f"Start file processing: {file_path}")  # Начало обработки файла

    try:
        with open(file_path, "r", encoding="utf-8") as f:

            trans_data_loger.info(f"File {file_path} successfully opened")  # Файл {file_path} успешно открыт

            transactions_json_data = json.load(f)

            trans_data_loger.info(f"File {file_path} successfully read")  # Файл {file_path} успешно прочитан

            if isinstance(transactions_json_data, list):

                trans_data_loger.info(
                    f"File {file_path} contains correct data"
                )  # Файл {file_path} содержит корректные данные

                return transactions_json_data

            else:
                trans_data_loger.warning(
                    f"File {file_path} does not contain a list of transactions"
                )  # Файл {file_path} не содержит список транзакций

                return []

    except (json.JSONDecodeError, OSError):
        trans_data_loger.error(
            f"Decoding error JSON in file {file_path}"
        )  # Ошибка декодирования JSON в файле {file_path}

        return []

file = '../src/operations.json'
print(load_json(file))