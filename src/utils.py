from typing import Any


def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевому слову"""
    filter_list_new = []
    for word in filter_words:
        for vac in vacancies_list:
            if word in vac.get("requirement"):
                filter_list_new.append(vac)
    return filter_list_new


def get_vacancies_by_salary(filtered_vacancies: Any, salary_range: Any) -> list:
    """Выдает списки вакансий сортированных по зарплате"""
    salary_list = salary_range.split("-")
    new_list = []
    for vac in filtered_vacancies:
        if int(salary_list[0]) <= vac["salary"] <= int(salary_list[1]):
            new_list.append(vac)
    return new_list


def sort_vacancies(vacancies_list: Any) -> list:
    """Сортировка вакансий"""
    sorted_vacancies = sorted(
        vacancies_list,
        key=lambda vacancies_list: vacancies_list["salary"],
        reverse=True,
    )
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: Any, top_n: Any) -> Any:
    """Топ вакансий"""
    if top_n == "":
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]


def print_vacancies(top_vacancies: Any) -> Any:
    dict_vac = []
    for vac in top_vacancies:
        dict_vac.append(
            f"\nВакансия: {vac.get('name')}\n"
            f"Ссылка: {vac.get('alternate_url')}\n"
            f"Зарплата: {vac.get('salary')}\n"
            f"Требования: {vac.get('requirement')}\n"
            f"Ответственность: {vac.get('responsibility')}\n"
            f"График: {vac.get('schedule')}\n"
            f"{'--'*20}"
        )
