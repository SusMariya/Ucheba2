import os.path
import pickle

class Atical:
    def __init__(self, title, autor, pages, description):
        self.title = title
        self.autor = autor
        self.pages =pages
        self.description =description

    def __str__(self):
        return f'{self.title} ({self.autor})'


class AticalModel:
    def __init__(self):
        self.db_name ='db.txt'
        self.aticals=self.load_data() # {'title': aticalc}

    def add_atical(self, dict_atical):
        atical =Atical(*dict_atical.values())
        self.aticals[atical.title] = atical

    def get_all_aticals(self):
        return self.aticals.values()

    def get_single_atical(self, user_title):
        atical = self.aticals[user_title]
        dict_atical = {
            "название": atical.title,
            'автор': atical.autor,
            'количество страниц': atical.pages,
            "описание": atical.description
        }
        return dict_atical

    def remuve_atical(self, user_title):
        return self.aticals.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.aticals, f)