# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:
#             a += str(i) + ", "
#         return f'Студент {self.name}: {a[:-2]}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def everange_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({"name": stud.name, "marks": stud.marks})
#         with open(filename, "w") as f:
#             json.dump(data, f, indent=2)
#
#
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = ""
#         for i in self.students:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @classmethod
#     def chenge_group(cls, group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, "w") as f:
#             stud_list=[]
#             for i in group.students:
#                 stud_list.append([i.name, i.marks])
#             tmp = {"Students": stud_list}
#             data.append(tmp['Students'])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def uploud_joirnal(cls, file):
#         with open(file, "r") as f:
#             print(json.load(f))
#
#
#
# st1 = Student('Bodnya', [5, 4, 5, 3, 5, 3])
# st2 = Student('Nikolaev', [3, 4, 3, 5, 3, 3, 3])
# st3 = Student('Birukov', [5, 4, 5, 4, 5, 4])
# # Student.dump_to_json(st1, "student.json")
# # Student.load_from_file("student.json")
# sts = [st1, st2]
# my_group = Group(sts, "гк Python")
# print(my_group)
# # my_group.dump_group("group.json", my_group)
# # Group.dump_group("group.json", my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st3]
# my_group2 = Group(group22, "ГК Web")
# Group.chenge_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
# my_group2.dump_group("group.json", my_group2)
# Group.uploud_joirnal("group.json")
#
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(1, 5)
# # print(st1)
# # print(st1.everange_mark())

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos") # найти данные с сервера
# todos = json.loads(response.text)
#
# # print(todos[:10])
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo ["completed"]:
#         try:
#             todos_by_user[todo["userId"]]+= 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key = lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complet in top_users:
#     if num_complet < max_complete:
#         break
#     users.append(str(user))
#
# max_users = " and ".join(users)
#
# s = "s" if len(users) > 1 else ""
# # print(users)
# print(f" user{s} completed {max_users} TODOs")
#
# def keep(todo):
#     is_completed = todo["completed"]
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
# with open("data.json", "w") as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open("data.json", "r") as f:
#     print(json.load(f))


# csv(comma separated values) разделитель

import csv

# with open("data.csv") as f:
#     reader = csv.reader(f, delimiter =";")
#     count = 0
#     for row in reader:
#         if count ==0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]}")
#         count+=1
#     print(f'Всего в файле {count} строки')

# with open("data.csv") as f:
#     fields_name = ["Имя", "Профессия", "Год рождения"]
#     reader = csv.DictReader(f, delimiter =";", fieldnames=fields_name) #
#     count = 0
#     for row in reader:
#         if count ==0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f'\t{row["Имя"]} - {row["Профессия"]}. ', end="")
#         print(f"Родился в {row['Год рождения']} году.")
#         count+=1
#     print(f'Всего в файле {count} строки')

# with open("student.csv", mode="w") as f:
#     writer = csv.writer(f, delimiter =",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco','3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]

# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open("sw_data.csv")as f:
#     print(f.read())

# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(data)
#
# with open("sw_data.csv")as f:
#     print(f.read())

# with open("student1.csv", mode="w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter =";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Женя", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), delimiter =";", lineterminator="\r")
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# #
import json

sl = {}


class St:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __str__(self):
        return f"{self.dictionary}"

    def add_dict(self):
        key = input('Введите страну: ')
        value = str(input('Введите столицу: '))
        self.dictionary[key] = value
        return self.dictionary

    def del_dict(self):
        key = str(input("Какую страну удалить? :"))
        del self.dictionary[key]
        return self.dictionary

    def seach_dict(self):
        key = input("Введите название страны: ")
        if key in self.dictionary:
            print(f"В стране {key} столица: {self.dictionary[key]}")
        else:
            print("Такой страны нет в словаре")

    def edit_dict(self):
        key = input("В какой стране изменить столицу?: ")
        if key in self.dictionary:
            value = input("Введите новую столицу: ")
            self.dictionary[key] = value
        else:
            print("Такой страны нет")

    def write_dictionary(self, x):
        try:
            data = json.load(open('dictionary.json'))
        except FileNotFoundError:
            data = {}

        data.update(self.dictionary)
        with open('dictionary.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=5)

    def load_dictionary(self):
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            print(json.load(f))

    def print_info(self):
        print(self.dictionary)


sl1 = St(sl)

print()
while True:
    option = input(
        "Выбирете действие:\n1 - Добавление данных\n2 - Удаление данных\n3 - Поиск данных"
        "\n4 - Редактирование данных\n5 - Сохранение данных\n6 - Просмотр данных\n\nВведите номер:  ")
    print()
    if option == "1":
        sl1.add_dict()
        print()
        sl1.print_info()
        print()
    elif option == "2":
        sl1.del_dict()
        print()
        sl1.print_info()
        print()
    elif option == "3":
        sl1.seach_dict()
        print()
    elif option == '4':
        sl1.edit_dict()
        print()
        sl1.print_info()
        print()
    elif option == '5':
        sl1.write_dictionary(sl1)
        print()
    elif option == '6':
        sl1.load_dictionary()
        print()
    else:
        break
