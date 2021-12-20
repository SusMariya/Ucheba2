# class Point:
#     """Класс для пердоставление координат точек на плоскости"""
#     x = 1
#     y = 1
#
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(getattr(p1, 'x'))
# Point.x = 100
# # print(p1.x, p1.y)
# # print(id(p1))
# # print(id(Point))
#
# p1.x = 5
# p1.y = 10
# # p1.z = 20
# print(p1.x, p1.y)
# # print(getattr(p1, 'z', "False"))
# setattr((p1, "z", 7))
# print(hasattr(p1, "x"))
# print(hasattr(p1, "z"))
# print(p1.__dict__)
# # print(Point.__dict__)
# # p2 = Point()
# # print(p2.x, p2.y)
# delattr(p1, "z")
# # print(p2.__dict__)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coords()
# p2 = Point()
# p2.set_coords()
# print(type(p1))
# print(type(p1) == Point)
# print(isinstance(p1, Point))

# или
# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x,y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
# p1 = Point()
# p1.set_coords(5, 10)
# p2 = Point()
# p2.set_coords(40, 80)
# Point.set_coords(3, 8)

# class Human:
#     name = "name"
#     birthsday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     adress = "Street, house"
#
#     def print_info(self):
#         print(" Персоанльный данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthsday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nАдрес: {self.adress}")
#         print("=" *40)
#
#     def input_info(self, name, birthsday, phone, country, city, adress):
#         self.name = name
#         self.birthsday = birthsday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.adress = adress
#
#     def set_name(self, name): # метод который устанавливает имя
#         """устанавливает имя"""
#         self.name = name
#
#     def ge_name(self): # метод получает имя
#         return self.name
#
#
# Human1 = Human()
# Human1.print_info()
# Human1.input_info("Юля", "23.05.1986", "45-65-98", "Россия", "Москва", "Чистопрудный перееулок, 1")
# Human1.print_info()
# Human1.set_name("Ирина")
# Human1.print_info()
# print(Human1.get_name())

# class Car:
#     name = "Car_name"
#     year = "Car_year"
#     model = "Car_model"
#     energi = "Car_energi"
#     color = "Car_color"
#     prise ="Car_prise"
#
#     def print_info(self):
#         print(" Данные автомобили ".center(40, "*"))
#         print(f"Название модели: {self.name}\nГод выпуска: {self.year}\n"
#               f"Производитель: {self.model}\nМощность двигателя: {self.energi}\n"
#               f"Цвет автомобиля: {self.color}\nЦена автомобиля: {self.prise}")
#         print("*"*40)
#
#     def input_info(self, name, year, model, energi, color, prise):
#         self.name = name
#         self.year = year
#         self.model = model
#         self.energi = energi
#         self.color = color
#         self.prise = prise
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#
# car1 = Car()
# car1.print_info()
# car1.input_info("Х7 М50i", "2021", "BMW", "530 л.с", "white", "10790000")
# car1.print_info()
# car1.set_model("Lada")
# car1.print_info()
# print(car1.get_model())

# class Person:
#     srill = 10 # квалификация сотрудника
#
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Данные сотрудника: {self.name} {self.surname}")
#
#     def add_skill(self, k):
#         self.srill += k
#         print(f"квалификация сотрудника {self.name} {self.srill}", )
#
#
# p1 =Person()
# p1.print_info("Viktor", "Reznik")
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info("Anna", "Dolgova")
# p2.add_skill(2)

# __магическийМетод__

#  Специальные методы
# конструктор __new__
# инициализатор __init__
# деструктор __del__


# class Point:
#
#     # def __new__(cls, *args, **kwargs):
#     #     print("Это конструктор")
#     #     return super().__new__(cls)
#
#     def __init__(self, x = 0, y = 0):
#         # print("Инициализатор")
#         self.x = x
#         self.y = y
#
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# Point.__init__(p1, 20, 50)
# print(p1.__dict__)
# # p2 = Point()
# # print(p2.__dict__)
# # p3 = Point(y = 2)
# # print(p3.__dict__)


# class Point:
#     count = 0
#
#
#     def __init__(self, x = 0, y = 0):
#         # print("Инициализатор")
#         self.x = x
#         self.y = y
#         Point.count+=1
#
#     def __del__(self):
#         print("Удаление экземпляра: " + self.__class__.__name__)
#
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point(2, 3)
# print(p2.__dict__)
# p3 = Point(2, 3)
# p4 = Point(2, 3)
# print(Point.count)
# print(p3.count)
# # print(p1.x)

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count+=1
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.x, self.y
#
# p1 = Point(5, 10)
# p1.set_coords("2", 3)
# # p1.set_coords(2, 3)
# print(p1.get_coords())
#
# print(p1.__dict__)

# Задача про роботов
# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k +=1
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -=1
#
#         if Robot.k == 0:
#             print(self.name, "Был последним")
#         else:
#             print("Работающих роботов осталось: ", Robot.k)
#
#     def say_hi(self):
#         print("Приветсвую! Меня зовут: ", self.name)
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов: ", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов: ", Robot.k)
# droid3 = Robot("PO")
# droid4 = Robot("C-3")
#
# print("\nЗдесь роботы могу проделать работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# del droid3
# del droid4
#
# print("Численность роботов: ", Robot.k)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def get_coords(self):
#         return self.__x, self.__y
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
# p1.set_coords_x(100)
# p1.set_coords_y(50)
# print(p1.get_coords())
# # print(p1.get_coords_x())
# # print(p1.get_coords_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)

#  Инкапсюляция
# x - public
# _x - протектед protected
# __ - private

# import math

# class Rectangle:
#     def __init__(self, length =1, width = 1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length*self.__width
#
#     def perimetr(self):
#         return (self.__length*self.__width)*2
#
#     def hypo(self):
#         return math.sqrt(self.__length**2 + self.__width**2)
#
#     def get_drow(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*"+ "\n")*self.__length)
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print("Длинна прямоугольника: ", rec1.get_length())
# print("Ширина прямоугольника: ", rec1.get_width())
#
# print("Площадь: ", rec1.square())
# print("Периметр: ", rec1.perimetr())
# print("Гипотенуза: ", round(rec1.hypo(), 2))
# rec1.get_drow()


# class Point:
#     WIDTH = 5
#     z = 100
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

# def __getattr__(self, item):
#     return f"В классе {__class__.__name__} отсувует атрибут: {item}"
#
# def __getattribute__(self, item):
#     if item =="_Point__x":
#         return "Закрытая переменная"
#     else:
#     #         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == "WIDTH":
#             raise AttributeError
#         else:
#             self.__dict__[key] = value
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def area(self):
#         return (self.__x*self.__y)+self.z
#
# p1 = Point(5, 10)
# # print(p1.zzz)
# # print(p1._Point_x)
# # print(p1.get_coords())
# # p1.set_coords(2, 3)
# # print(p1.get_coords())
# p1.z = 100
# # Point.WIDTH = 10
# print(p1.area())

# 16/12/2021
# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             ValueError("Неверный формат данных")
#
#     def __get_coords_x(self):
#         print("Вызывается __get_coords_x")
#         return self.__x
#
#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 100
# print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property # геттер (getter) важен порядок
#     def coords_x(self):
#         print("Вызывается __get_coords_x")
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             ValueError("Неверный формат данных")
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# del p1.coords_x
# p1.coords_x = 7
# # print(p1.coords_x)
# print(p1.__dict__)

# задача перевест килогрммы в фунты

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.kg)
# print(w.to_pounds())
# w.kg = "десять"
# print(w.to_pounds())


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count+=1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x+1
#
#     @staticmethod
#     def dec(x):
#         return x-1
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))

# class Nambers:
#     @staticmethod
#     def max(x, y, z, w):
#         if x>y and x>z and x>w:
#             return "Максимальное число ", x
#         elif y>x and y>z and y>w:
#             return "Максимальное число ", y
#         elif z>x and z>w and z>x:
#             return "Максимальное число ", z
#         else:
#             return "Максимальное число ", w
#     @staticmethod
#     def min(x, y, z, w):
#         if x<y and x<z and x<w:
#             return "Минимальное число ", x
#         elif y<x and y<z and y<w:
#             return "Минимальное число ", y
#         elif z<x and z<w and z<x:
#             return "Минимальное число ", z
#         else:
#             return "Минимальное число ", w
#
#     @staticmethod
#     def sred(x, y, z, w):
#         return "Среднее значение", (x + y +z +w)/4
#
#     @staticmethod
#     def faktorial(x):
#         fac = 1
#         for i in range(1, x + 1):
#             fac *= i
#         return f"Факориал числа", fac
#
#
# print(Nambers.max(1, 2, 3, 4))
# print(Nambers.min(1, 2, 3, 4))
# print(Nambers.sred(1, 2, 3, 4))
# print(Nambers.faktorial(4))

# class Date:
#     def __init__(self, day = 0, month = 0, year = 0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
# # d = "16.12.2021"
# # day, month, year = map(int, d.split("."))
# # print(day, month, year)
# # date = Date(day, month, year)
# date = Date.from_string("16.12.2021")
# print(date.string_to_db())
# date1 = Date.from_string("17.12.2021")
# print(date1.string_to_db())

# class Date:
#     def __init__(self, day = 0, month = 0, year = 0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
# date =[
#     '30.12.2021'
#     '38-12-2020'
#     '01.01.2021'
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print("Неправильный формат даты")
#


# class Ploshad:
#     count = 0
#     @staticmethod
#     def S_Geron(a, b, c):
#         Ploshad.count +=1
#         perimetr = (a+b+c)/2
#         return (perimetr*(perimetr-a) * (perimetr-b) * (perimetr-c))**0.5
#
#     @staticmethod
#     def s_Treyg(a, h):
#         Ploshad.count += 1
#         return 0.5* h * a
#
#     @staticmethod
#     def S_sq(e):
#         Ploshad.count += 1
#         return e**2
#
#     @staticmethod
#     def S_pramoyg(a, b):
#         Ploshad.count += 1
#         return a*b
#
#
# print(Ploshad.S_Geron(3, 4, 5))
# print(Ploshad.s_Treyg(6, 7))
# print(Ploshad.S_sq(7))
# print(Ploshad.S_pramoyg(2, 6))
# try_t = Ploshad()
# print(try_t.S_Geron(1, 2, 3))
# print(Ploshad.count)





