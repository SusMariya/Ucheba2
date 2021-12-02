# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y])
#
# a = {
#     "John": {
#         "N": "3056",
#         "S": "8443",
#         "E": "8441",
#         "W": "2694"
#     },
#     "Tom": {
#         "N": "4835",
#         "S": "6786",
#         "E": "4737",
#         "W": "2694"
#     },
#     "Anna": {
#         "N": "3056",
#         "S": "8443",
#         "E": "8441",
#         "W": "2694"
#     },
#     "Mary": {
#         "N": "3056",
#         "S": "8443",
#         "E": "8441",
#         "W": "2694"
#     },
# }
# print(a)
# name_s = input("Введите имя: ")
# name_r = input("Введите регион: ")
#
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y])
# # if name_r in a:
# #     print({})
# s = int(input("Введите новое значение: "))
# a[name_s][name_r] = s
# print(s[name_s])
        # Дописать из записи

# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print(f'\t{y}: {a[x][y]}')
#         # print('\t', y, ':', a[x][y])

# a = {'один': 1, 'два': 2, 'Три': 3, 'четыре': 4}
# d = {value: key for key, value in a.items()}
# print(d)
# d = {key: value for key, value in a.items() if value <= 2}
# print(d)

# a={i: i*5 for i in [10, 20, 30, 40]}
# print(a)

# s = "Hello"
# b = {i: i*3 for i in s}
# print(b)

# value = input('-> ')
# lst = [1, 2, 3, 4]
# d ={k: value for k in lst}
# print(d)

# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
# print(m)
# print(m.get())
# try:
#     print(m{(2, 0)})
#
#
# if (2, 1) in m:
#     print(m[(2, 0)])
# else:
#     print(0)
#
# SciPy
# list()
# a = {1:"Rectangle", 2: "Triangle", 3: "Ciecle"}
# value = list(a.value()) # Список значения словаря
# print(value)
#
# k = list(a.keys()) # Список ключей словаря
# print(k)
#
# par = list(a.items()) # список пар ключ:значение
# print(par)


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# zip

# b = dict(zip([1, 2, 3], ["two", "one", "three"]))
# print(b)

# a = ["Dec", "Jan", "Feb"]
# b = [12, 1, 2]
# # d = {k: v for (k, v) in zip(a, b)}
# d =zip(a, b)
# # print(dict(d))
# print(list(d))

# print(list(zip(range(5), range(5))))
#
# a = {12: "Dec", 1: "Jan", 2: "Feb"}
# b = {3: "Match", 4: "April", 5: "May"}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, "-> ", v1)
#     print(k2, "-> ", v2)

# pairs = [(1,  'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# ls = [4, 2, 1, 3]
# n = ['c', 'b', 'd', 'a']

# a = list(zip(ls, n))
# print(a)
# a.sort()
# print(a)
# a = list(zip(n, ls))
# print(a)
# a.sort()
# print(dict(a))
# a = sorted(zip(ls, n))
# print(a)
#
# mohth =["J", "Fr", "Ma"]
# total = [52000.00, 51000.00, 48000.00]
# prod = [46800.00, 45900.00, 43200.00]
#
# for t, p, m in zip(total, prod, mohth):
#     profit = t - p
#     print("Общая прибыль В", m, "=", profit)
#
# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})
#
# for k,v in {**one, **two}.items():
#     print(k, "-> ", v)

# data = [5, 6, 7, 8, 9, 1, 4]
# for i, val in enumerate(data, 1):
#     print(i, ")", val)

data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 1, 7: 4}
for i, val in enumerate(data, 1):
    print(i, ":", data[val])

d = {"1": {'a': 1, 'b': 2, 'c': 3},
    "2": {'a': 10, 'b': 20, 'c': 30}}
for i, k in enumerate(d, 10):
    print(i, ") key =", k, ", value = ", d[k], sep="")
print(i)