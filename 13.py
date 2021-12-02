# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))


# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))
#
# a = [1, 2, 3]
# b = [ 4, 5,*a, 6]
# print(b)

# def func(*args):
#     return args
#
# print(func(1))
# print(func(1, 2, 3, "abc"))
# print(func())
#
# def summa(*par):
#     # res = 0
#     # for n in par:
#     #     res += n
#     # return res
#     return sum(par)
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))

# def func(*el):
#     return {i: i for i in el}
#
# print(func(1, 2, 3, 4))

# def func(*el):
#     a = sum(el)/len(el)
#     return {i: i for i in el if i < a}
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def func(a, b, *args):
#     return a, b, args
#
# print(func(1, 2))
# print(func(1, 2, 3, "abc"))


# def print_scores(stu, *scores):
#     print("Имя студента: ", stu)
#     for s in scores:
#         print(s, end = " ")
#     print()
#
#
# print_scores("Валентин", 100, 95, 88, 92, 89)
# print_scores("Роман ", 96, 86, 75, 89, 56)


# def revers_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2 != 0):
#             res.append(revers_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def func(**kwargs):
#     return kwargs
#
# print(func(a = 1,b = 3, c = 2))
# print(func(a = "Python"))
# print(func())


# def func(*args, **kwargs):
#     return args, kwargs
#
#
# print(func(4, 6, a=1, b=3, c=2))
# print(func(a="Python"))
# print(func())

# def info(**data):
#     for k, v, in data.items():
#         print(k, "is", v)
#     print()
#
# info(firstname="Irina", lastname="Sharma", age=22, phon="12345679")
# info(firstname="Igor", lastname="Wood", email= "igor@mail.ru", contry="Rassia", age=25, phon="49996857412")
#
#
# my_dict={'one':'first'}
# def db(**kwargs):
#     my_dict.update(**kwargs)
#     return my_dict
#
# db(k1=22, k2e=31, k3=11, k4=91)
# print('my_dict =', db(name='Bob', age=31, weight=61, eye_color='grey'))


# def pet_names(name, **pets):
#     print("Name: ", name)
#     for pet, name in pets.items():
#         print(pet, ":", name)
#
#
# pet_names("Jonathan", dog="Brock", fish=["lorry", "Curly", "Molly"], turtle="Sheldon")
#
# def func(name, **args, odd=False, **kwargs):
#     return name, args, odd, kwargs
#
# print(func("Irina", 1, 2, 3, 4, odd = True, one="1", three="3"))

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, 'one': 1, 'two': 2, **y}
print(z)
