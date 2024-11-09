def get_top_vacancies(sorted_vacancies, top_n):
    '''Топ вакансий'''
    if top_n == '':
        return sorted_vacancies
    else:
        return sorted_vacancies[0:int(top_n)]

def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевому слову"""
    filter_list_new = []
    for vac in vacancies_list:
        for word in filter_words:
            if vac['description'] is None:
                continue

            elif word in vac["description"] or word in vac["name"]:
                filter_list_new.append(vac)
        return filter_list_new