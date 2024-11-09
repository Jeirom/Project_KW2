import json




class JSONSaver:
    def __init__(self, filename = 'operations.json'):
        self.filename = f'/data/{filename}'

    def writer(self, vacancy):
        with open(self.filename, 'w') as f:
            json.dump(vacancy, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, new_vacancy) -> None:
        with open(self.filename, 'w') as f:
            json.dump(new_vacancy, f, ensure_ascii=False, indent=4)

