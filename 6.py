# lst = [5, 3, 2, 4, 1]
# print(" Длинна списка", len(lst))
# print("Минимальное значение", min(lst))
# print("Максимальное значение", max(lst))
# print("Сумма", sum(lst))

# import random as r
# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print("Max", max_1)
# mas1.remove(max_1)
# mas1.insert(0, max_1)
# print(mas1)

import random as r
mas1 = [r.randint(-20, 20) for i in range(10)]
print(mas1)
mas1.sort(reverse = True)
print(mas1)

# import random as r
# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# min_1 = min(mas1)
# print("Мin", min_1)
# ind_min_l = mas1.index(min_1)
# print("Index_min", ind_min_l)
#
# del mas1[0:ind_min_l]
# print(mas1)
# print(mas1[ind_min_l:])

# in - оператор принадлежности
# not in - не содержется ли

# x = list('drovsmoeio320')
# print(x)
# print('a' in x)
# print('2' in x)
# print('a' not in x)
# print('0' not in x)

# lst = []
# if not lst:
#     print("Список пустой")
# else:
#     print("")

# import random as r
#
# n = int(input("Ведите длинну первого списка:"))
# m = int(input("Ведите длинну второго списка:"))
# mas1 = [r.randint(0, 10) for i in range(n)]
# mas2 = [r.randint(0, 10) for i in range(m)]

# print("первый список", mas1)
# print("второй список", mas2)
# mas3 = mas1 + mas2
# print("третий список", mas3)
# mas3 = []
# # for i in range(len(mas1)):
#     if mas1[i] not in mas3:
#         mas3.append(mas1[i])
# for i in range(len(mas2)):
#     if mas2[i] not in mas3:
#         mas3.append(mas2[i])
# print("Элементы обоих списокв без повторений", mas3)
# mas3 = []
# for i in mas1:
#     repeat = False
#     for j in mas2:
#         repeat = True
#     if not repeat:
#         mas3.append(i)
# for i in mas2:
#     repeat = False
#     for j in mas1:
#         repeat = True
#     if not repeat:
#         mas3.append(i)
# print("Элементы обоих списокв без повторений", mas3)
# mas3 =[]
# for i in range(len(mas1)):
#     if mas1[i] in mas2 and mas1[i] not in mas3:
#         mas3.append(mas1[i])
# print("Элементы обоих списокв без повторений", mas3)
# mas3 = []
# mas3 = [min(mas1), min(mas2), max(mas1), max(mas2)]
# print(mas3)
# print("Список без повторений:")
# listVal5 = []
# listVal5 += [i for i in mas1 if mas1.count(i) == 1]
# listVal5 += [i for i in mas2 if mas2.count(i) == 1]
# print(listVal5)
# print("Общие элементы")
# listVal6 = [i for i in mas1 if i in mas2]
# print(listVal6)



# us1 = ["Игoрь", "Мария", "Владимир", "Алла"]
# us2 = us1
# us2.append("Виктория")
# print(us1)
# print(us1s2)
# is - возвращает True, если оба операнда указывают нна один и тот же объект
 # is not - возвращает True, если оба операнда указывают на разные объекты

# us2 = copy.deepcopy(us1)
# us2.append("Виктория")
# print(us1)
# print(us2)

# m = [
#     [1, 2, 3, 4], # -нулевая строка кода
#     [5, 6, 7, 8],  # -первая строка кода
#     [9, 10, 11, 12] # - вторя строка
# ]
# print(m[1][2])
# m[row][col]
# print(m)

# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end ="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end = "\t")
#     print()

# m = [
#     [1, 2, 3, 4], # -нулевая строка кода
#     [5, 6, 7, 8],  # -первая строка кода
#     [9, 10, 11, 12] # - вторя строка
# ]
# m = [[ for x in range(y, y+10]for row in range(10)]:
# for row in m
#         print(x, end = "\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x+y)

# m =[
#     [1, 2, 6],
#     [3, 4, 3],
#     [5, 6, 4],
#     [7, 8, 8]
# ]
# for i in range(len(m)):
#     if (i-1)%2 == 0:
#         m[i].sort()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()

# import random as r
# w, h = 5,4
# m = [[r.randint(1, 30) for x in range(w)] for x in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# import random as r
# w, h = 3, 4
# m = [[r.randint(-20, 10) for x in range(w)] for x in range(h)]
# count = 0
# for row in m:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             count +=1
#     print()
# print("Количество отрицательных значений", count)
