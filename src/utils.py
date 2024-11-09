from src.api_class_hh import HeadHunterAPI
from src.vacancy import Vacancy
from typing import Any

def get_top_vacancies(sorted_vacancies, top_n):
    """Топ вакансий"""
    if top_n == '':
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]

def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевому слову"""
    filter_list_new = []
    for word in filter_words:
        for vac in vacancies_list:
            if word in vac.get("requirement"):
                filter_list_new.append(vac)
    return filter_list_new

def get_vacancies_by_salary(filtered_vacancies, salary_range):
    salary_list = salary_range.split(" - ")
    new_list = []
    for vac in filtered_vacancies:
        if int(salary_list[0]) <= vac["salary"] <= int(salary_list[1]):
            new_list.append(vac)
    return new_list

def sort_vacancies(vacancies_list: Any) -> list:
    """Сортировка вакансий по зарплате. Больше зп - выше место в списке"""
    sorted_vacancies = sorted(vacancies_list, key=lambda vacancies_list: vacancies_list["salary"], reverse=True)
    return sorted_vacancies

def get_top_vacancies(sorted_vacancies, top_n):
    """Топ вакансий"""
    if top_n == '':
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]

def print_vacancies(top_vacancies):
    """Принтует конечный результат в терминал."""
    pass


if __name__ == "__main__":
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.load_vacancies("Python")

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)