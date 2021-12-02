# декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'hello'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# # test = my_decorator(func_test)
# # test()
# func_test()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#     return wrap
# #
# @italic
# @bold
#
# def hello():
#     return "test"
#
# print(hello())

# def deco(fn):
#     counter = 0
#     def wrapper():
#         nonlocal counter
#         fn()
#         counter += 1
#         print('Вызов функции', counter)
#
#     return wrapper
#
#
# @deco
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# def arg_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
# @arg_decorator
# def print_full_name(a, b, c = "Виктор", study = "Pyton"):
#     print(a, b, c, "изучает", study, "\n")
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study="Javascript")
# print_full_name("Владимир", "Екатерина")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("*" *20)
#         print(*args)
#         fn(*args)
#         print("*" *20)
#     return wrap
#
# @args_decorator
# def one(a, b):
#     print(a+ b)
#
#
# @args_decorator
# def two(a, b, c):
#     print(a * b * c)
#
#
# one(2, 3)
# two(2, 3, 4)
# two(2, 3)
#
# def args_decorator(arg1, arg2):
#     print("Я создаю декоратор. Аргументы: ", arg1, arg2)
#     def my_dekorator(func):
#         print("Я - декоратор. Аргументы", arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print("Я - обортка вокруг декарурующей фуекции")
#             func(arg1, arg2)
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_dekorator
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_name(first, last):
#     print("Меня зовут:", first, last)
#
#
# print_full_name("Ирина", "Лавровва")

# def args_decorator(decorator_text):
#     def my_dekorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_dekorator
#
# @args_decorator(decorator_text="hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world("world!")


# def decor(num):
#     def my_dekor(func):
#         def wrap(args):
#             return "Результат: " + str(func(args * num))
#
#
#         return wrap
#
#     return my_dekor
#
# @decor(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Типы данных не соответсвуют")
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Типы данных не соответсвуют")
#
#             return fn(*f_args, **f_kwargs)
#         return wrap
#
#     return wrapper
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2("Hello, ", "wolrd", "!"))
# print(typed_fn3("Hello, ", "wolrd! ", z=5))

# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#         return wrap
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
# @args_decorator
# def hello_wolrd(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_wolrd2(text):
#     print(text)
#
# hello_wolrd("Hi")
# hello_wolrd2("wolrd")


# print(int('19'))
# print(int(19.5))
# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19)) # двоичная система
# print(oct(19)) # восьмиричная система
# print(hex(19)) # шеснадцатиричная система исчесления
#
# print(0B1010)
# print(0o12)
# print(0xA)
#
# q = "Pyt"
# w = 'hon'
# e = q+w
# print(e)
# print(e * 3)
#
# print(e in "I am learn Python")
# print(e in "I am learn Java")
#
# s = "Hello"
# print(s[1])
# print(s[-1])
# print(s[1:6])
# print(s[1:4])
# print(s[:4])
# print(s[2:])
# print(s[2:-1])
# print(s[2:len(s)])
# print(s[2:len(s)-1])
# print(s[2:2])
# print(s[2:3])
# print(s[4:0:-2])
# print(s[0:4])
# print(s[::-1])
#
# s = 'abcdefgh'
# print(s[slice(2, 5)])
# print(s[slice(5, )])
# print(s[slice(5, None)])
# print(s[slice(5, None, -1)])
# print(s[slice(None, None, 2)])
# print(s[slice(None, None, -1)])

# s = 'python'
# print(id(s))
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# def chande_char(s, c_old, c_new):
#     print(str1.replace('Nuthon', 'Python'))
#
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интрересный язык программирования"
# chande_char(str1, "N", "P")
# print(str1)

# def chande_char(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 +c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#
#     return s2
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интрересный язык программирования"
# str2 = chande_char(str1, "N", "P")
# print(str1)
# print(str2)

# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
#
#
# def renam(stroka, start, chenge):
#     a = ""
#     for i in range(len(stroka)):
#         if stroka[i] == start:
#             a = a[:i] + chenge
#         else:
#             a = a[:i] + stroka[i]
#     return a
#
#
# print(str1)
# print(renam(str1, "N", "P"))

# print(u"Hello")
# print('I\'m learning\n Python')
# print('C:\\file.txt')
# print(r'C:\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')
# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}, мне {age} лет")

# import math
# print(f"Значение числа pi: {math.pi:.2f}")
# x = 10
# y = 5
# print(f"{x}*{y}/2 = {x * y/2}")

# planats = ["Меркурий", "Венера", "Земля", "Марс"]
# print(f'Мы живем на плнете {planats[2]}')
#
# planat = {"name": "Земля", "radius": 6378000}
# print(f"Планета {planat['name']}. Радиус {planat['radius']/1000} км.")
#
#
# print(f"13 / 3 = {round(13/3)}")


# name = "друг"
# prof = "программист"
# lang = "Python"
#
# massage= (
#     f"Привет {name}."
#     f"Ты {prof}."
#     f"На языке {lang}"
# )
#
# print(massage)

# a = 74
# print(f"{{{{{74}}}}}")
#
# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)
#
# s = '5'
# s1 = "2"
# print("мне " + str(s) + " лет")
# print(min(s, s1))
# print(max(s, s1))
#
#
# s = 'Hello'
# s1 = "hel"
# print(max(s, s1))
# print(sum(s, s1))

# print(ord('a')) # 97
# print(ord('#')) # 35
#
#
# print(ord('у')) # 1091
#
#
# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break



# str = "Test string for me"
# arr = [ord(x) for x in str]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr)/len(arr))] +arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in (input("-> "))[0:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Кличество последних элементов: ", arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(35))

# a =122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

a =122
b = 97
print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a+1)))