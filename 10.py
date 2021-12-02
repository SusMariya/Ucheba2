# множество - set()
# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
b = {}
a = set('hello')
print(type(a))
print(type(b))
print(a)
c = ["red", "green", "blue", "purple"]
col = set(c)
# print(col)
#
# s = {x*x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = list({i for i in numbers if i % 2 ==0})
# print(num)

# def to_set(a):
#     b = set(a)
#     return b, len(b)
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
#
# c = {"red", "green", "blue", "purple"}
# print("green" not in c)

# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")

# r1 = ["ab_1", "ac_2", "bc_1", "bc_2"]
# # a = {i for i in r1 if "a" not in i}
# a = {"A" + i[1:]
#      if i[0] == 'a' else 'B' + i[1:]
#      for i in r1
#      if i[1] == 'c'}
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  # добавление елемента
# print(a)
# a.remove(4)  # удаление элемента
# print(a)
# b = 6
# if b in a:
#     a.remove(6)
# print(a)
#
# a.discard(1) # удаление элемента без генерации сключенияб если элемент отсутсвует
# print(a)
#
# a.pop() # удаление первого элемента
# print(a)
#
# a.clear() # полная очистка
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = b | a
# a.update(b)
# b |= a
# c = a.intersection(b)
# a &= b
# a -= b
# c = a ^ b
# a ^= b
# c = a <= b
# c = a >= b
# c = a != b
# c = a.copy()
# print(c)
# print(b)


# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# i = {6}
# f = {7, 8}
# g = {9, 8}
# s = a | b | c | d | i | f | g
# print(s)
# print("Количество уникальных", len(s))
# print("минимальное", min(s))
# print("максимальное", max(s))
#
# el1 = set(input("Введите первую строку: ", ))
# el2 = set(input("Введите вторую строку: ", ))
# c = el1 & el2
# for i in c:
#     print(i, end=" ")

# s1 = {"Марина", "Женя", "Света"}
# s2 = {"Костя", "Женя", "Илья"}
# s3 = s1 ^ s2
# print("В одном кружке", s3)
# s4 = s1 & s2
# print("Во всех кружках", s4)
# # s1.remove("Женя")
# s5 = s2 - s4
# print("Женя ушел из кружка", s5)

# тип frozentset (замороженное множество)
# s = frozenset({1, 2, 3, 4, 5})
# print(s)
# print(2 in s)

# s = frozenset({i ** 2 % 4 for i in range(10)})
# print(s)

# r1 = set('ABCD')
# b = {frozenset({i+j for j in r1.difference({i})}) for i in r1}
# print(b)

def superset(s1, s2):
    if s1 > s2:
        print("Объект ", s1, " является чистым супермножеством")
    elif s1 == s2:
        print("множества равны")
    elif s2 > s1:
        print("Объект ", s2, " является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")
set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)
