# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("перед вызовом функции")
#             print(self.name)
#             func(a, b)
#             print("после вызова функции")
#
#         return wrap
#
#
# @MyDecorator("test2")
# def function(a, b):
#     print(a, b)
#
#
# function(2, 5)


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)
#             return res ** 2
#         return wrapper
#
#
# @Power(3)
#
# def mulpuhl(a, b):
#     return a*b
#
# print("Резульат", mulpuhl(2,2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*"*20)
#         fn(*args, **kwargs)
#         print("*"*20)
#     return wrap
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
# p1 = Person("Вителий", "Карасев")
# p1.info()


#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def dec(fn):
#         def wrap(*args, **kwargs):
#             print("*" * 20)
#             fn(*args, **kwargs)
#             print("*" * 20)
#
#         return wrap
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
# p1 = Person("Вителий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))

# class Messenge:
#     _REGISTRY= {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def registor(cls, name):
#         def decorator(klass):
#             cls._REGISTRY[name] = klass
#             return klass
#         return decorator
#
#     @classmethod
#     def cread(cls, messenge_typ, text):
#         klass = cls._REGISTRY.get(messenge_typ)
#         if klass is None:
#             raise ValueError("такого месенджера нет")
#         print(text, end = "")
#         return klass(text)
#
# @Messenge.registor('Telegram')
# class TelegranMesseng(Messenge):
#     def send(self):
#         print("(Telegram)")
#
#
# @Messenge.registor('Whatsap')
# class WhatsapMesseng(Messenge):
#     def send(self):
#         print("(Whatsap)")
#
# # m1 = TelegranMesseng("text")
# m1 = Messenge.cread("Telegram", "text")
# m1.send()
# m3 = Messenge.cread("Whatsap", "new text")
# m3.send()
# # m2 = WhatsapMesseng("new text")
# # m2.send()

# Дискриптор

# __get__() / __set__() / __delete__()  / __set_name__()
# Дискриптор данных или data descriptor
# non-data descriptor (дескриптор не данных ) - только для __get__

# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person("Иван", "Николаев")
# print(p.surname)
# print(p.name)

# ============= это же =>

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)  # экземпляр класса
#         self.surname = String(surname)  # экземпляр класса
#
#
# p = Person("Иван", "Николаев")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())


# ================================================
# __get__() / __set__() / __delete__()  / __set_name__()

# class ValidString:
#     def __set_name__(self, owner, name):  # owner = ссылка на класс Person
#         self.__name = name
#
#     def __get__(self, instance, owner):  # owner = ссылка на класс Person, instance = ссылка на экземпляр класса
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()  # экземпляр класса
#     surname = ValidString()  # экземпляр класса
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Николаев")
# print(p.name)
# p.name = "Игорь"
# print(p.name)
# print(p.surname)

# == ЗАДАЧА
# Дискриптор данных или data descriptor
# class NoNegative:
#     def __set_name__(self, owner, name):  #
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     price = NoNegative()
#     quantity = NoNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())
# apple.price = -10

# ============= МЕТТАКЛАССЫ - класс который создает другие классы

# a = 5
# print(type(a))
# print(type(int))

# =============================

# class MyList(list):  # если наследуется от list, можем применять методы списков (append())
#     def get_length(self):
#         return len(self)
#
#
# lst=MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# тоже самое =>
# # MyList = type(
# #     'MyList',
# #     (list,),
# #     dict(get_length=lambda self:len(self))
# # )

# ===============

# class MyMetaclass(type):
#     def __new__(mcs, name, bases, attr):  # Конструктор,  mcs = метакласс, имя, bases-от чего наследуем, аттрибуты
#         print("Создание нового объекта", name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, bases, attr)
#
#     def __init__(cls, name, bases, attr):  # первым параметром cls
#         print("Инициализация класса", name)
#         super(MyMetaclass, cls).__init__(name, bases, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print(stud.get_name())
# print(type(stud))
# print(type(Student))

import 30.py
30.main()

# e = 30.ElectroCar("Tesla", 'T', 2018, 99000)
# e.show_car()
# e.description_batarry()