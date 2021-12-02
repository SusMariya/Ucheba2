# day = int(input("Введите день недели цифрами: "))
# if 1 <= day <= 5: #(day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or 7:
#     print("Рабочий день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 8:
#         print("воскресенье")
# else:
#     print("Такого дня недели нет!")

# mun = int(input("Введите месяц в году цифрами: "))
# if 1 <= mun <= 2 or mun == 12:
#     print("Зима")
# elif 3 <= mun <= 5:
#     print("Весна ")
# elif 6 <= mun <= 8:
#     print("Лето")
# elif 9 <= mun <= 11:
#     print("Осень")
# else:
#     print("Такого месяца нет!")

# a, b = 20, 10
# minim = a if a < b else b
# print(minim)

# a, b = 20, 20
# print( "a == b" if a ==b else "a > b" if a>b else "a < b")

# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# print( "Делить на ноль нельзя" if b == 0 else a/b)

# try:
#     a = int(input("Введите целое число: "))
#     print((a *2))
# except ValueError:
#     print("что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n/m))
# except (ValueError, ZeroDivisionError):
#     print("нельзя вводить строки")
#     print("нельзя делить на ноль")
# else:
#     print("Все нормально. Вы ввели числа", n, " и", m)
# finally:
#     print("конец программы")
#
# n = input("Введите 1 число: ")
# m = input("Введите 2 число: ")
# try:
#     n = int(n)
#     m = int(m)
#
# except (ValueError):
#    n = str(n)
#    m = str(m)
# finally:
#     print(n + m)

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1
# i = 20
# while i > 0:
#     print("i =", i)
#     i -= 2

# n = int(input("Введите количество симолов: "))
# r = ""
# while n > 0:
#     r += "*"
#     n -= 1
#     print(r)

# a=1
# while True:
#     n = int(input("Введите число: "))
#     if not n != 0:
#         break
#     a *= n
# print("Результат", a)

# i = 0
# while i < 10:
#     # if i ==5:
#     #     break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i=", i)

# i = 1
# while i < 10:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 10:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i += 1

i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i, "*", j, "=", i*j, "\t\t", end="")
        j += 1
    print()
    i += 1
