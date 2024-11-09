from src.api_class_hh import HeadHunterAPI
from src.json_saver import JSONFileHandler


def user_interface():
    """Функция, реализующая взаимодействие с пользователем через консоль"""
    api = HeadHunterAPI()
    file_handler = JSONFileHandler()
    while True:
        print("\n1. Получить вакансии")
        print("2. Добавить вакансии в файл")
        print("3. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies = api.get_vacancies(keyword)
            for vacancy in vacancies:
                print(
                    f"Название: {vacancy['name']}, Ссылка: {vacancy['alternate_url']}, Зарплата: {vacancy['salary']}"
                )
        elif choice == "2":
            keyword = input("Введите ключевое слово для поиска вакансий: ")
            vacancies = api.get_vacancies(keyword)
            formatted_vacancies = [
                {
                    "title": v["name"],
                    "url": v["alternate_url"],
                    "salary": v["salary"]["from"] if v["salary"] else None,
                    "description": v["snippet"]["responsibility"],
                }
                for v in vacancies
            ]
            file_handler.save_data(formatted_vacancies)
            print("Вакансии добавлены в файл.")
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    user_interface()