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


class Point:
    WIDTH = 5
    z = 100

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # def __getattr__(self, item):
    #     return f"В классе {__class__.__name__} отсувует атрибут: {item}"
    #
    # def __getattribute__(self, item):
    #     if item =="_Point__x":
    #         return "Закрытая переменная"
    #     else:
    #         return object.__getattribute__(self, item)
    def __setattr__(self, key, value):
        if key == "WIDTH":
            raise AttributeError
        else:
            self.__dict__[key] = value

    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coords(self, x, y):
        if Point.check_val(x) and Point.check_val(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def set_coords_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")

    def set_coords_y(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")
    def get_coords(self):
        return self.__x, self.__y

    def area(self):
        return (self.__x*self.__y)+self.z

p1 = Point(5, 10)
# print(p1.zzz)
# print(p1._Point_x)
# print(p1.get_coords())
# p1.set_coords(2, 3)
# print(p1.get_coords())
p1.z = 100
# Point.WIDTH = 10
print(p1.area())