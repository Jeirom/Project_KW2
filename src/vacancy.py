import json
class Vacancy:

    __slots__ = ("name", "alternate_url", "salary", "requirement")

    def __init__(self, name, alternate_url, salary, requirement):
        self.name = name
        self.alternate_url = alternate_url
        self.salary = self.__validation_salary(salary)
        self.requirement = requirement

    @staticmethod
    def __validation_salary(salary):
        if salary:
            return salary
        return {"salary": {"from": 0, "to": 0}}

    @classmethod
    def cast_to_object_list(cls, vacancies: list):
        new_list = []
        for vacancy in vacancies:
            name = vacancy.get("name")
            alternate_url = vacancy.get("alternate_url")
            requirement = vacancy.get("requirement")
            if vacancy.get("salary") is None or vacancy.get("salary").get("from") is None:
                salary = 0
            else:
                salary = vacancy.get("salary").get("from")
            dict_vac = {"name": name,
                        "alternate_url": alternate_url,
                        "salary": salary,
                        "requirement": requirement}
            new_list.append(dict_vac)
        return new_list

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Vacancy(data['title'], data['link'], data['salary'], data['description'])


    def __le__(self, other, file_list):
        new_file = []
        for i in file_list:
            if other <= i["salary"]["from"]:
                new_file.append(i)
        return new_file