# import math as m
#
# num = m.sqrt(2)
# print(num)
# num1 = m.ceil(3.8)
# print(num1)
# num2 = m.floor(3.8)
# print(num2)

# from math import sqrt, ceil, floor
# #
# num = sqrt(2)
# print(num)
# num1 = ceil(3.8)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# from math import *
# #
# num = sqrt(2)
# print(num)
# num1 = ceil(3.8)
# print(num1)
# num2 = floor(3.8)
# print(num2)

# from math import pi
# print(pi)

# from math import pi as p
# print(p)

# from math import *
# radius = 2
# print(pi*(radius**2))

# from math import *
# n = int(input("Ведите радиус окружности: "))
# print(floor(pi*n*2))
# print(round((pi*n*2),2))


from math import *


# num = -5.24
# print("Модуль числа: ", fabs(num))

# a = -14
# b = -8
# print("Наибольший общий делитель: ", gcd(a, b))

# num_list = [0.3, 0.3, 0.3]
# print("Сумма элементов списка: ", fsum(num_list))
# print("Сумма элементов списка: ", sum(num_list))
# # decimal
# print(degrees(3.14159265))
# print(radians(180))
# print(cos(radians(60)))
# print(tan(radians(45)))
#
# a = int(input("Катет 1: "))
# b = int(input("Катет 2: "))
# print(sqrt((a**2)+(b**2)))
#
# print("Вычеслите площадь фигур \nВыбор фигуры: \n1- треугольник \n2- прямоугольник \n3-круг ")
# a = int(input("Ведите номер фигуры: "))
# if a == 1:
#     b = int(input("Ведите сторну a: "))
#     c = int(input("Ведите сторону b: "))
#     d = int(input("Ведите сторну c: "))
#     print("Площадь треугольника: ", (d+b+c)/2)
# if a == 2:
#     f = int(input("Ведите длину a: "))
#     k = int(input("Ведите ширину b: "))
#     print("Площадь прямоугольника: ", (f*k))
# if a == 3:
#     w = int(input("Ведите радиус: "))
#     print("Площадь круга: ", round(pi*(w**2),2))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
#
# sec = time.time()
# print("Секунды с начала эпохи", sec)
# local_time = time.ctime(sec)
# print("Местное время: ", local_time)
# res = time.localtime(sec)
# print("Локальное время: ", res)
# print("Год: ", res.tm_year)
# print("Месяц: ", res.tm_mon)
# print("День месяца: ", res.tm_mday)
# print("Часы: ", res.tm_hour) # c 0 до 23
# print("Минуты: ",  res.tm_min)  # с 0 до 59
# print("Секунды: ", res.tm_sec) # с 0 до 61
# print("День недели: ", res.tm_wday) # С 0 до 6
# print("День года по счету: ", res.tm_yday) # с 1 до 366
# print("Учет перехода на летнее время: ", res.tm_isdst) # 0или 1 или -1

# print((time.strftime("Today is %d %b,  %Y", time.localtime(484961819))))
# print(time.strftime("%m/%d/%Y, %I:%M:%S"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(str(pause) + " seconds.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print("Program time: " + str(res) + " second.")


# start = time.monotonic()
# time.sleep(1)
# finish = time.monotonic()
# res = finish - start
# print("Program time: " + str(res) + " second.")

# print((time.strftime("Сегодня %d %B,  %Y")))


### Функции

# def hello(name, word):
#     print("Hello, ", name, ". Say " + word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y =3
# get_sum(x,y)
# get_sum(2.6, 4.3)
# get_sum("gfjg", "koub")
# get_sum(str(x), "koij")

# def symbol(count, a, b):
#     for i in range(count):
#         if i %2 ==0:
#             print(a, end =" ")
#         else:
#             print(b, end =" ")
#     print()
#
#
# symbol(8, "+", "-")
# symbol(7, "x", "0")

def get_sum(a, b):
    # return a+b
    # print("текст")
    print(a+b)


x = 2
y =3
# res = get_sum(x,y)
# print(res)
print(get_sum(2.6, 4.3))
# get_sum("gfjg", "koub")
# get_sum(str(x), "koij")

