import re

#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio=fio
#         self.old=old
#         self.password=ps
#         self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split() # f = ["Фамилия", "Имя", "Отчество"]
#         if len(f)!=3:
#             raise TypeError("Неверный формат ФИО")
#         letters= "".join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE)) # ФамилияИмяОтчество
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters))!=0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old,int) or old<14 or old>100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float))or w<26:
#             raise TypeError("Вес должен быть числом от 20 кг и выше")
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps,str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         print(s)
#         if len(s)!=2 or len(s[0])!=4 or len(s[1])!=6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password= ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self,weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# # Фамилия Имя Отчество
#
# # p1 = UserData("Волков2 Игорь Николаевич", 26, "1234 123456", 88.8)
# # p1 = UserData("Волков-Петров Игорь Николаевич", 26, "1234 123456", 88.8)
#
# # p1 = UserData(10, 26, "1234 123456", 88.8)
# # p1 = UserData("Волков-Петров Игорь Николаевич qqq", 26, "1234 123456", 88.8)
# p1 = UserData("Волков Игорь Николаевич", 16, "1234 123456", 36)
# p1.fio = "Соболев Игорь Николаевич"
# p1.old = 50
# p1.weight = 160
# p1.password = "1258 845632"
# print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координаты должны быть целыми числами")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()
# line.set_coords(Point(4, 56), Point(5, 6))
# line.draw_line()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self,sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#     def set_coords(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()
# line.set_coords(Point(4, 56), Point(5, 6))
# line.draw_line()



# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self): # абстрактный метод
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellips(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50,50), Point(100, 100)))
# figs.append(Ellips(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()

from math import pi

class Table:

    def __init__(self, width=None, length=None, radius=None):
        if radius is None:
            self._width = width
            self._length =length
        else:
            self._radius = radius

    def set_radius(self, radius):
        self._radius = radius

    def set_sides(self, width = None, length=None):
        if length is None:
            self._width = self._length = width
        else:
            self._width=width
            self._length = length

    def calc_area(self):
        raise NotImplementedError("В дочернем классе должен быть определено метод calc_area")

class Sq_table(Table):
    def calc_area(self):
        return self._width * self._length

class Round_table(Table):
    def calc_area(self):
        return pi*self._radius**2

t = Sq_table(20, 10)
t.set_sides(2,1)
print(t.__dict__)
print(t.calc_area())

t1 = Round_table(radius=10)
print(t1.__dict__)
print(t1.calc_area())

t2 = Round_table(radius=20)
t2.set_radius(60)
print(t2.__dict__)
print(t2.calc_area())
