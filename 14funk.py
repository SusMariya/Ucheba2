# def outer_fanc(who):
#     def inner_func():
#         print("Hello, ", who)
#     inner_func()
#
#
# outer_fanc("world")
# outer_fanc("star")

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренний функции", a+b)
#
#     print("Значение внешней переменной a: ", a)
#     fun2(4)

# fun1()

x = 25


# def fn():
#     global t
#     a = 30
#
#     print("global: ", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal: ", a)
#         return
#     inner()
#     t = a
#     return
#
# fn()
#
# z = x + t
# print(z)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
# result = outer(2, 3, -1, 4)
# print("result = ", result)

# s = 0
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_psquare(i, j):
#         nonlocal s
#         s += i * j
#
#
#     rect_psquare(a, b)
#     rect_psquare(a, c)
#     rect_psquare(b, c)
#     return 2*s
#
# print(rect_paral_square(2, 4, 6))
# print("s = ", s)
# print(rect_paral_square(5, 8, 2))
# print("s = ", s)
# print(rect_paral_square(1, 6, 8))
# print("s = ", s)
#
# def increment(number):
#     def inner_increment():
#         return number+1
#     return inner_increment()
#
# print(increment(10))

# # closur (замыкание)
# def increment(n):
#     def inner_increment(x):
#         return n +x
#     return inner_increment
#
# a =increment(12)
# print(a(5))
# # print(increment(12)(5)) # не используют, но оно работает

#
# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a+ 1
#         b = b +"1"
#         return a, b, c
#
#     return func2
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s+= 1
#         print(city, s)
#
#     return inner
#
# res1 = func('Москва')
# res1()
# res1()
# res2 =func('Сочи')
# res2()
# res2()

# studens = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
# def mace_classfilter(lower, upper):
#     def class_studens(exem):
#         return {k: v for (k,v) in exem.items() if lower <= v <= upper}
#
#     return class_studens
#
#
#
# a = mace_classfilter(80, 100)
# b = mace_classfilter(70, 80)
# c = mace_classfilter(50, 70)
# d = mace_classfilter(0, 50)
# print(a(studens))
# print(b(studens))
# print(c(studens))
# print(d(studens))

def func(a, b):
    def add():
        return a + b

    def sub():
        return a - b

    def mul():
        return a*b

    def replace():
        print()

    replace.add = add
    replace.sub = sub
    replace.mul = mul
    return replace

obj1 = func(5, 2)
print(obj1.add())

obj2 = func(5, 2)
print(obj2.sub())

obj3 = func(5, 2)
print(obj3.mul())