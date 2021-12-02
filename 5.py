# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("----------------------")
# for i in my_list:
#     print(i ** 2, end=" ")
# print("\n----------------------")
# for i in range(len(my_list)):
#     my_list[i] = my_list[i] ** 2
#     print(my_list[i], end=" ")

# a = int(input("Введите количество элементов: "))
# b = [int(input("-> ")) for i in range(int(input("n = ")))]
# if b[i] < 0:
#     sum += b
# print("сумма: ", sum)

# n = list(range(21, 41))
# print("Список: ", n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество:  ", k)
# print("Сумма: ", s)

# b = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = s = 0
# for i in range(len(b)):
#     if b[i] != 0:
#         k += b[i]
#         s += 1
# print("Середнеарифметическое от не нулевых: ", k/s)

# Срезы - получение какой-то части списка, которая в свою очередь тоже является списком

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:4])
# print(s[::2])
# print(s[::-1])
# print(s[5:0:-1])
# print(s[-2:2:-1])
# print(s[-1:4:-1])

# s =[1, 2, 3, 4, 5, 6, 7]
# print(s[:-1:-1])
# print(s[::2])
# print(s[1:7:2])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[-3:-6:-1])
# print(s[-3:1:-1])

# s =[1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# s[1:2] = [20]
# s[8] = [20]
# s[9:10] = [20]
# s[19:20] = [18]
# print(s)
# s.append(99)   # добавляет элемент в конец списка
# s.append(['abb', 2])
# print(s)
# s1 = []
# s1.extend([1,2,3]) # добавляет множество элементов
# print(s1)
# s1.extend('abb')
# print(s1)

# n = []
# n.extend(i ** 2 for i in range(1, 11))
# print(n)

# num_array = []
# for i in range(1, 11):
#     num_array.extend([i ** 2])
# print(num_array)

# s.insert(1, 100) # добавляет элемент в список в заданную позицию (первый параментр) и с указанным значением (второй параметр)
# print(s)

# s1 =[]
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     s1.append(x)
# print(s1)

# s =[]
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится без остатка на 3")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print("Результат: ", c)

# s = [5, 9, 2, 1, 4, 3, 2, 4]
# s[7:]=[]
# print(s)
# s.remove(2) # удаляем элемент из списка с заданным значением, если элементов несколько то удалится только первый
# print(s)
# # s.remove(6)
# print(s)

# s[3:5] = []
# print(s)
#
# last = s.pop() # возвращает элемент на указанные позиции, удаляя его из списка
# print(last)
# print(s)
#
# second = s.pop(-2)
# print(second)
# print(s)
#
# s.clear() # удаляет из списка все имеющиеся значения, список остается
# print(s)
#
# del s[1]
# print(s)
# s =[]
# s.extend([3, 6, 8, 5, 65, 99, 8])
# print(s)
# num = s.count(3) # считает количество значений "3" в списке
# print(num)
#
# ind = s.index(3) # возвращает положение первого индекса
# print(ind)

# s_copy = s.copy() # возвращает копию списка
# print(s)
# print(s.copy)

# a =[1, 2, 3]
# b = a
# print("a = ", a)
# print("b = ", b)
# a.append(20)
# print("a = ", a)
# print("b = ", b)

# s.append(120)
# print(s)
# print(s.copy)

# s.reverse() # перестраивает список в обратном порядке
# print(s)

# s.sort(reverse = True) # сортиирует список, если указать  reverse = True то по убыванию список сортирует
# print(s)

# sorted_s = sorted(s, reverse=True)
# print(sorted_s)
# print(s)

# b = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(b)
# k = int(input("введите элемент: "))
# b1 = b.remove(k)
# b2 = b.sort()
# print(b)

# from random import random, randint, randrange
# print(random()) # [0.0, 1.0]
# print(randint(0, 9))
# print(randrange(0, 10, 2))

import random as r
print(r.randint(0, 5))
print(r.randint(0, 5))
print(r.randrange(0, 10, 2))

citys =["Москва ", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
print(r.choice(citys))

s =[55, 66, 77, 99, 58, 469, 66, 17]
print(r.sample(s, 3))
print(r.choices(s, k=5))

r.shuffle(s)
print(s)

print(round(r.uniform(10.5, 25.5), 2))

mas =[r.randint(0, 100) for i in range(10)]
print (mas)