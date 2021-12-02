# словари (dict)
# a = [1, 2, 3, 4]
# b = {"one":1, "two":2}
# print(b)

# d3 = dict.fromkeys(['a', 'b'], 100)
# print(d3)
#
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)


# d4 = {a: a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4[2])


# d4 = {str(a): a ** 2 for a in range(2, 7)}
# print(d4)
# print(d4["2"])
# d4["2"] = 15
# print(d4)
# d4["5"] = 4 ** 2
# print(d4)


# d5 = {0: "text1", "one": 40, (1, 2.3): 'картеж', 40: [2, 3, 6, 7], True: 1}
# print(d5)
# # print(d5["two"][1])
# print(d5[(1,2.3)])
# del d5[(1, 2.3)]
# print(d5)
#
# print("one" in d5)
# print("a" in d5)
#
# print(d5.keys())
#
# if 'one' in d5:
#     print("TRUE")
# if 'one' in d5.keys():
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6["four"])
# key = "four"
# if key in d6:
#     del d6[key]
# print(d6)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# # print(d6["four"])
# key = "four"
# try:
#     del d6[key]
# except KeyError:
#     print('Элемент с ключем "'+key + '" нет в словаре')
# print(d6)

# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "=", d6[key])

# d7 ={'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# count = 1
# for key in d7:
#     print(key, "=", d7[key])
#     count *=d7[key]
# print(count)
# b = a['x1'] * a['x2'] * a['x3'] * a['x4']

# d = dict()
# # d[1] = input("-> ")
# # d[2] = input("-> ")
# # d[3] = input("-> ")
# # d[4] = input("-> ")
# for k in range(1,5):
#     d[k] = input("-> ")
# print(d)
# s = int(input("Выбирете элемент для удаления: "))
# del d[s]
# print(d)

#
# f = {'one': 1, 'two': 2, 'three': 3}
# print(len(f))


# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
#
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print("Столица страны: " + country + ": " + capitals[country])
#     else:
#         print("В базе нет страны с названием: " + country)

goods = {
    "1": ['Core-i3 - 4330', 9, 4500],
    "2": ['Core-i5 - 4670k', 3, 8500],
    "3": ['AMD FX - 6300', 6, 3700],
    "4": ['Pentium G3220', 8, 2100],
    "5": ['Core-i5 - 3450', 5, 6400]
}

for i in goods:
    print(i, ")", goods[i][0], " - ", goods[i][1], " шт.по ", goods[i][2], " руб.", sep="")
s = 1
while True:
    s = int(input("№ "))
    if s == 0:
        break
    goods[s][1]=input("Количество - ")
for i in goods:
    print(i, ")", goods[i][0], " - ", goods[i][1], " шт.по ", goods[i][2], " руб.", sep="")


# iter

# d = {"A": 1, "B": 2, "C": 3}
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
# d.clear()
# print(d)

# d2 = d.copy()
# print("d= ", d)
# print("d2= ", d2)
# d2["B"] =5
# d["E"] =7
# print("d= ", d)
# print("d2= ", d2)
#
# value =d.get("E") # получение значения по заданому ключу
# print(value)
#
# new =d.items() # список пар ключей со значением
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys() # сисок ключей словаря
# print(a)
#
# item = d.pop("E", 5)
# print(d)
# print(item)

# item = d.setdefault("S", 5) #  устанавливается элемент по умолчанию
# print(item)
# print(d)

# d.update([('R', 7), ('Q', 9)])
# print(d)
# d.update([('A', 20), ('B', 40)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = {'q': 5, 'b': 10}
# z = {i: d[i] for d in [x, y] for i in d}
# v = z.values()
# lst = list(v)
# z = x|y|c
# z = x.copy()
# z.update(y)
# print(z)
# print(lst)