# def hi(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(hi(10, 5))
# print(hi(5, 15))
#
# # hi()
# print(hi())

# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         pass
#
# print(maxmin(10, 5))
# print(maxmin(5, 15))


# s1 = int(input("s1: "))
# s2 = int(input("s2: "))
#
#
# def maxmin(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(maxmin(s1, s2))


# def hi(a):
#     return a ** 3
#
# for i in range(1, 11):
#     print(i, " в кубе= ", hi(i))

# def fib(n):
#     a, b = 0, 1
#     while a< n:
#         print(a, end=" ")
#         a, b = b, a + b
#     print()
#
# fib(22)
# fib(61)

# def fib(n):
#     a, b = 0, 1
#     while a< n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#     print()
#
# fib(22)
# fib(61)

# def chenge(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(chenge([1, 2, 3]))
# print(chenge([9, 12, 33, 54, 105]))
# print(chenge(["c", "л", "о", "н"]))


# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))

# def get_sum(a, b, c, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2))

# def get_sum(a, b, c=0, d=1): # аргументы по умлочанию
#     return a + b + c + d
#
#
# x, y, z = 1, 5, 6
# print(get_sum(1, 5))
# print(get_sum(x, y, d = z)) # именованные (ключевые) параметры

# def n(a, b):
#     return a * b
#
#
# print(n(20, "+"))

# def check_password(username, password, min_length=8, check_username=True):
#     if len(password) < min_length:
#         print("Пароль слишком короткий")
#         return True
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "пароль прошел проверку")
#         return True
#
#
# check_password("Igor", '12345')
# check_password("Igor", '12345Igor', check_username=False)
# check_password("Igor", '12345name')

# def a(n, even=True):
#     s = 0
#     while n > 0:
#         b = n % 10
#         if even and b % 2 == 0:
#             s += b
#         elif not even and b % 2 != 0:
#             s += b
#         n //= 10
#     return s
#
#
# print("Сумма четных элементов")
# print(a(9874023))
# print(a(38271))
# print(a(123456789))
# print("Сумма нечетных элементов")
# print(a(9874023, even=False))
# print(a(38271,even=False ))
# print(a(123456789, even=False))


# def display_info(name, age):
#     print("Name: ", name, "\nAge: ", age, "\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age =23, name="Ira")

# def func(a, ln =[]): # ln=[] или ln = list()
#     ln.append(a)
#     return ln
#
# print(func(1))
# print(func(2))
# print(func(3))

# def func(a, ln=None):
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))

# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(id(a1))
# print(id(a2))
# print(a1 == a2)
# print(a2 is a1)

# a3 = "Hallo"
# a4 = "Hallo"
# print(id(a3))
# print(id(a4))
# print(a3 == a4)
# print(a4 is a3)

# a1 = [1, 2, 3]
# print(id(a1))
# a1.append(4)
# print(a1)
# print(id(a1))
# a1[1] = "Hello"
# print(a1)
# print(id(a1[1]))

# s = "Hello"
# print(id(s))
# s += "World" #s = s+"World
# print(s)
# print(id(s))

#
# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# st = "hello"
# print(id(st))
# st= st[1: -1]
# print(st)
# print(id(st))
#
# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(id(a1))
# print(id(a2))
# y = a1
# print(id(y))
# # print(a1 == a2)
# print(a1 is a2)
# # print(a1 == y)
# print(a1 is y)
# a1[0] = 0
# print(a1)
# print(y)

# x = [1, 2, 3]
# y = x[:]
# print(y)
# y[0] = 0
# print(y)
# print(x)
# print(id(y))
# print(id(x))

# x = [1, 2, 3]
# print(id(x))
# x += [4, 5]
# print(x)
# print(id(x))


def add_namber(n):
    print("Внутри функции: ", n, "=", id(n))
    n += [4]
    print("После присваивания: ", n, "=", id(n))

x = [1, 2, 3]
print(x, "=", id(x))
add_namber(x)
print(x, "=", id(x))