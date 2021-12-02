# print((lambda x, y: x+y)(1, 2))

# func = lambda x, y: x + y
# print(func(1, 2))
# print(func("a", "b"))

# print((lambda x, y: (x**2)+(y**2))(2, 5))

# summ = lambda a =1, b = 2, c = 3: a +b +c
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# print(summ(10, 20, 30))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1("a", "b"))

# c = (lambda x: x*2,
#      lambda x: x*3,
#      lambda x: x*4)
#
# for t in c:
#     print(t('abc'))

# def inc(n):
#     return lambda x: x + n
#
# inc = (lambda n: (lambda x: x + n))
#
# f = inc(42)
# print(f(0))
# print(f(10))
#
# print((lambda n: (lambda x: x + n))(42)(10))

# print((lambda n: (lambda x: (lambda y: x + n + y)))(2)(4)(6))

# d = {'c': 4, 'b':15, 'a': 10}
# list_d = list(d.items())
# print(list_d)
# list_d.sort(key=lambda i: i[1])
# print(list_d)
# print(dict(list_d))

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#      {'name': 'Алексе   ', 'last name': 'Бодня', 'rating': 10},
#      {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#      {'name': 'Михайил', 'last name': 'Семенов', 'rating': 6}
#      ]
#
# res = sorted(players, key = lambda item: item['last name'])
# print(res)
# res1 = sorted(players, key = lambda item: item['rating'], reverse=True)
# print(res1)
# res2 = sorted(players, key = lambda item: item['rating'])
# print(res2)
# d_players = list(players.items())
# print(d_players)

# a = [
#      (lambda x, y: x+y),
#      (lambda x, y: x-y),
#      (lambda x, y: x*y),
#      (lambda x, y: x/y)
# ]
# b = a[1](5, 12)
# print(b)

# a = [lambda x, y: x+y, lambda x, y: x-y, lambda x, y: x*y, lambda x, y: x/y]
# b = a[1](5, 12)
# print(b)

# a = {'one': lambda x: x-1, 'two': lambda x: abs(x)-1, 'three': lambda x:x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: lambda: print('Mandey'),
#     2: lambda: print('Truesdey'),
#     3: lambda: print('Wendey'),
#     4: lambda: print('Twerdey'),
#     5: lambda: print('Fridey'),
#     6: lambda: print('Saturdey'),
#     7: lambda: print('Sundey'),
#
# }
# d[2]()

# import math
# a = {
#      'circle': lambda r: math.pi*r*r,
#      'pr': lambda x, y: x*y,
#      'tr': lambda x, y, z: (x+y)/2*z
# }
#
# print('Площадь окружности: ', a['circle'](2))
# print('Площадь прямоугольника: ', a['pr'](10, 13))
# print('Площадь трапеции: ', a['tr'](10, 13, 5))

# TRUE if условие else FALSE

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 13))
# print(maximum(5, 13))


# print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 8, 5))

# def mul(t):
#     return t*2
#
# lst = [2, 8, 12, -5, 10]
# # lst2 =list(map(mul, lst))
# # print(lst2)
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))
# print(lst2)

# areas = [3.65897, 5.547892, 4.809146, 56.24587, 9.8123488, 32.569874]
# res = list(map(round, areas, range(1, 5)))
# print(res)
#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: [x, y], st, num))
# print(res)

# st = [1, 2, 3]
# num = [4, 5, 6]
# res = list(map(lambda x, y: [x + y], st, num))
# print(res)

# st = 'hello'
# res = list(map(lambda x: x, st))
# print(res)

# t = ('asdfg', 'asd', 'asde', 'fd', 'aqw')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 37, 76, 60, 88, 88, 74, 81, 65]
# res = list(filter(lambda s: s> 75, b))
# print(res)

# b = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda s: 10 <= s <= 20, b))
# print(res)

# import random as r
# lst =[r.randint(1, 40) for i in range(10)]
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst)
# print(res)
#
# b = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, b))) # или print(list(filter(lambda s: not s % 15, b)))

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)

# b = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], b))
# print(m)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
#
# a = """Тройные "двойные" кавычки"""
# b = '''три одинаковые кавычки'''
# print(a)
# print(b)

import math
def cilindr(r, h):
    """
    вычисляет площадь цилиндра.

    Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
    :param r: положительное число, радиус основания цилиндра
    :param h: положительное число, высота цилиндра
    :return: положительное число, возвращает пллощадь цилиндра
    """
    return 2 * math.pi * r * (r + h)

print((cilindr(3, 6)))
print(cilindr.__doc__)
print(max.__doc__)
