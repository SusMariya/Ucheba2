# # кортеж (tuple) похожа на список, список для чтения
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(tpl)
#
# a = ()
# print(type(a))
#
# b = tuple()
# print(type(b))
#
# # упаковка кортежа
# a1 = (5,)
# print(type(a1))
# c = 1, 2, 3
# c = tuple((1, 2, 3))
# print(type(c))
# print(c)
#
#
# t1 = tuple("Hello")
# print(t1)


# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])


# s1 = tuple(int(input("->")) for i in range(5))
# print(s1)

# s = input("Введите по порядку, без пробела элементы кортежа: ")
# a = tuple(s)
# print(a)

# import random as r
# mas = tuple([r.randint(0, 100) for i in range(10)])
# # a = tuple(mas)
# print(mas)


# import random as r
# mas = tuple([2**i for i in range(1, 13)])
# print(mas)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index("l"))
# # print(t3.index("a"))
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print("Такого симовола нет")

# for i in t3:
#     if i == " ":
#         continue
#     print(i, end=" ")

def slicer(tpl, el):
    if el in tpl:
        if tpl.count(el) > 1:
            f = tpl.index(el)
            s = tpl.index(el, f+1)
            return tpl[f:s+1]
        else:
            return tpl[tpl.index(el):]
    else:
        return ()


print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# import random as r
# mas1 = tuple([r.randint(0, 5) for i in range(10)])
# mas2 = tuple([r.randint(-5, 0) for i in range(10)])
# print(mas1)
# print(mas2)
# mas3 = mas1 + mas2
# print(mas3)
# print("0= ", mas3.count(0))

# import random as r
# def ran(a, b):
#     return tuple(r.randint(a, b) for i in range(10))
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("]0= ", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))

# def ran(a):
#     b = []
#     [b.append(i) for i in reversed(ran) if i not in b]
#     return tuple(b)
#
# print(ran([1, 2, 3, 3, 2]))
# print(ran([2,1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# распаковка кортежа
# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)
#
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])
#
# a = tuple((1, 2, 3, 4, 5))
# del a
#
# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)
# print(ls)

# contries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(contries)
# for contry in contries:
#     contryName, contryPopuletion, citis = contry
#     print("\nСтрана: ", contryName, "население= ", contryPopuletion)
#     for city in citis:
#         cityName, cityPopuletion =city
#         print("\tГород", cityName, "население= ", cityPopuletion)

