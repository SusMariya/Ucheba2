# УПАКОВКА ДАННЫХ: Сериализаци и Десериализации

# import pickle  # распространенный


#
# filename = 'basket.txt'
#
# shop_list = {
#     'Фрукты': ["яблоки", "манго"],
#     'Овощи': ["морковь"],
#     "Бюджет": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop_list, fh) #сохраняет данные в файл (делает не читабильные данные)
#
# with open(filename, "rb") as fh:
#     print(pickle.load(fh)) # считывает данные из файла

#
# class Test:
#     a_namber = 35
#     a_strinh = "привет"
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f'Число: {Test.a_namber}\nСтрока: {Test.a_strinh}\nСписок: {Test.a_list}\nКортеж: {Test.a_tuple}' \
#                f'\nСловарь: {Test.a_dict}'
#
# obj = Test()
#
# my_obj = pickle.dumps(obj) #сохраняет данные в оперативную память loads- считывает данные из оперативной памяти
# print(f"Сериализация в строку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация данных в строку:\n{l_obj}\n")


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         print(attr)
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x *x
#
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# сичтать и пронумировать строки в файле
# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding="utf - 8")
#         self.count = 0
#
#     def red_line(self):
#         self.count+=1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith("\n"):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state =self.__dict__.copy()
#         del state["file"]
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
# reader = TextReader("Hello.txt")
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())

# import json

# data = {
#     'firstName': "Jane",
#     'lastName': "Djo",
#     'hobbies': ("running", "sky diving"),
#     'age': 5,
#     "20": "one"
# }

# with open("data_file.json", "w") as fw:
#     json.dump(data, fw, indent=4)
#
# with open("data_file.json", "r") as fw:
#     print(json.load(fw))
#
# st = json.dumps(data, sort_keys=True)
#
# data = json.loads(st)
# print(data)

# x=

import json
from random import choice

def gen_person():
    name = ''
    tel = ''


    letters = ['a', 'b', 'd', 'b', 'e', 'f', 'e', 'g']
    nam = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # while len(name)!=7:
    #     name +=choice(letters)
    # print(name)
    #
    # while len(name)!=10:
    #     name +=choice(letters)
    # print(name)


    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nam)
    person = {
        'name': name,
        'tel': tel
    }
    return person

def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileExistsError:
        data = []

    data.append(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


persons = []
for i in range(5):
    # persons.append(gen_person())
    write_json(gen_person())

# with open('persons.json', 'a') as f:
#     json.dump(persons, f, indent=2)