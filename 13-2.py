# name ="Tom"
# def hi():
#     print("Hello,", name)
#
# def bye():
#     print("Good bye,", name)
#
# hi()
# bye()
#
# name ="Tom"
# def hi():
#     global name
#     name = "Sam"
#     print("Hello,", name)
#
# def bye():
#     print("Good bye,", name)
#
# hi()
# bye()

# def add_two(a):
#     x = 2
#     return a + x
#
# print(add_two(3))
# print(x)
#
# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x= ", x)
#         return a + x
#     return wrap()

# print(add_five(5))


# x = 4
#
#
# def func():
#     print(x + 3)
#
#
# func()

# x = 4
#
#
# def func():
#     a = 3
#     print(x + a)
#
#
# func()

import builtins

names = dir(builtins)
for i in names:
    print(i)