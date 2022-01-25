# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <=item<len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key <0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None]* off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise IndexError("Индекс должен быть целым число")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# print(s1.marks)
# del s1[2]
# print(s1.marks)


# class Point30:
#     CH = "Доблжно быть целым числом"
#     RIGHT = "Правый операнд должен типом Point30"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#     @staticmethod
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float) # isinstance(v, (int,float))
#
#     @staticmethod
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("Координаты не должны быть равны нулю")
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):
#         if not isinstance(other, Point30):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point30(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point30):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point30(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point30):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point30(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point30):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point30(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):
#         if not isinstance(other, Point30):
#             raise ValueError(self.RIGHT)
#         return Point30(self.__x == other.x and self.__y == other.y and self.__z == other.z)
#
#     def __getitem__(self, item):  # print("x = ", pt['x'], "x 1= ", pt2['x'])
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.x
#         elif item == "y":
#             return self.y
#         elif item == "z":
#             return self.z
#         else:
#             print('Неверное значение ключа')
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key =="x":
#                 self.__x = value
#             elif key == "y":
#                 self.__y = value
#             elif key == "z":
#                 self.__z = value
#             else:
#                 print("Координаты должны быть числами")
#
# pt = Point30(12, 15, 18)
# pt2 = Point30(6, 3, 9)
# print(f"Координаты первой точки: {pt}")
# print(f"Координаты второй точки: {pt2}")
#
# pt3 = pt + pt2
# print(f"Сложение координат: ({pt3})")
# pt4 = pt - pt2
# print(f"Вычитание координат: ({pt4})")
# pt5 = pt * pt2
# print(f"Умножение координат: ({pt5})")
# pt6 = pt / pt2
# print(f"Деление координат: ({pt6})")
#
# print(f"Равенство координат: ({pt==pt2})")
# print("x =", pt['x'], "x1 =", pt2['x'])
# print("y =", pt['y'], "y1 =", pt2['y'])
# print("z =", pt['x'], "z1 =", pt2['z'])
#
# pt['x'] = 20
# print("Запись значение по координаты: x=", pt['x'] )
# print("Координаты первой точки:", pt)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_reg_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_reg_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# shape = [r1, r2, s1, s2]
#
# for g in shape:
#     print(g.get_reg_perimetr())


# class Namber:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value +int(a)
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
# t1 = Namber(10)
# t2 = Text("Pithon")
# print(t1.total(35)) #45
# print(t2.total(35)) #8

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         print(f'{self.name} мяукает')
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f'Я сабака. Меня зовут {self.name}. Мой возраст {self.age}')
#
#     def make_sound(self):
#         print(f'{self.name} гавкает')
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.__class__}: {self.name}'

    def __str__(self):
        return f' {self.name}'


cat = Cat("Пушок")
print(cat)

