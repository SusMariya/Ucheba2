# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_euro = "EURO"
#
#     def __init__(self, surname, nam, persent, value = 0):
#         self.surname = surname # фамилия владельца
#         self.nam = nam # номер счета
#         self.persent = persent # процент начисления
#         self.value = value # сумма в рублях
#         print(f'Счет #{self.nam} принадлежащий {self.surname} был открыт')
#         print("*"*50)
#
#     def __del__(self):
#         print(f'Счет #{self.nam} принадлежащий {self.surname} был закрыт')
#
#     @classmethod
#     def set_usd_rate(cls, rate): # рудактирование курса рубля по отношению к доллару
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate):  # рудактирование курса рубля по отношению к евро
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_ower(self, surname): # смена владельца счета
#         self.surname = surname
#
#
#     def convert_to_usd(self): # перевод в доллары
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_euro(self): # перевод в евро
#         euro_val = Account.convert(self.value, Account.rate_euro)
#         print(f"Состояние счета: {euro_val} {Account.suffix_euro}")
#
#     def add_persent(self):
#         self.value +=self.value *self.persent
#         print("Проценты были успешно начислены!")
#         self.print_balans()
#
#     def withdraw_money(self, val): # сняние заданной суммы
#         if val >self.value:
#             print(f"К сожалению у вас нет такой {val} {Account.suffix}")
#         else:
#             self.value-=val
#             print(f"{val} {Account.suffix} были успешно сняты!")
#         self.print_balans()
#
#     def add_money(self, val):
#         self.value +=val
#         print(f"{val} {Account.suffix} были успешко добавлены!")
#         self.print_balans()
#
#     def print_balans(self):
#         print(f"Текущий юаланс: {self.value} {Account.suffix}")
#
#     def print_info(self): # вывод информации о счете
#         print("Информация о счете")
#         print("-"*20)
#         print(f'#{self.nam}')
#         print(f'Владелец: {self.surname}')
#         self.print_balans()
#         print(f"Проценты: {self.persent:.0%}")
#         print("-" * 20)
#
#
#
#
# acc =Account("Долгих", 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_euro()
#
# Account.set_usd_rate(2)
# Account.set_euro_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_euro()
# print()
# acc.edit_ower("Дюма")
# acc.print_info()
# print()
# acc.add_persent()
# print()
# acc.withdraw_money(3000)
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}" # или return str(self.x)
# class Prop:
#     def __init__(self, sp: Point, ep:Point, color:str = "red", width: int= 1):
#         print("Инициализатор базового класа Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args) # или так как ниже
#         super().__init__( *args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
# class Rect(Prop):
#     def draw_Rect(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)
# # print(Line.width)
# # Line.width = 10
# # print(Line.width)
# # Line.draw_line()
# # Line = Rect(Point(38, 40), Point(10, 20))
# # Line.draw_Rect()
#
# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}" # или return str(self.x)
# class Prop:
#     def __init__(self, sp: Point, ep:Point, color:str = "red", width: int= 1):
#         print("Инициализатор базового класа Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         # Prop.__init__(self, *args) # или так как ниже
#         super().__init__( *args)
#         self.__width = 5
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")
#
# class Rect(Prop):
#     def draw_Rect(self):
#         print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.__width}")
#
# line = Line(Point(1, 2), Point(10, 20))
# print(line.__dict__)
# # print(Line.width)
# # Line.width = 10
# # print(Line.width)
# line.draw_line()
# # Line = Rect(Point(38, 40), Point(10, 20))
# # Line.draw_Rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w>0:
#             self.__width=w
#         else:
#             raise ValueError("Значение ширины должно быть больше нуля")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def heigth(self, h):
#         if h>0:
#             self.__height = h
#         else:
#             raise ValueError("Значение высоты должно быть больше нуля")
#
#     def border_new(self):
#         return self.border_new
#
#     def area(self):
#         return self.__width*self.__height
#         return self.color
#         return self.border_new()
#
# rect = Rectangle(10, 20, "green", "1px solid gray")
# print(rect.area())
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.border)
# rect.width = 50
#
# print(rect.width)
# print(rect.area())
#
# class Liqvid: # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density # плотность жидкости
#
#     def edit_density(self, val): # изменение плотности
#          self._density = val
#
#     def calc_v(self, m): # вычесление объема жидкости в соответсвии заданой массе
#         res = m/self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v): # вычесление массы жидкости соответвующее заданному объему
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} составляет {res} kg')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} (плотность равна {self._density} kg/m^3).')
#
# class Alcohol(Liqvid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength # крепость
#
#     def edit_strength(self, val): # изменение крепости
#         self.strength = val
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(500)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(70)
# print(a.strength)

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
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
# class Prop:
#     def __init__(self, sp: Point, ep:Point, color:str = "red", width: int =1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width =width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Кооординаты дожны быть числами")
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"РИсование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coords(self, sp: Point, ep: Point):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Кооординаты дожны быть целыми числами")
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30.2, 40), Point(100, 200))
# line.draw_line()

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}')
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка: ", self.fon)
#
# class ReckBorder(Rect):
#     def __init__(self, width, height,  border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка: ", {self.border})
#
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# shape1 = ReckBorder(400, 200, "1px")
# shape1.show_rect()

# class Liqvid: # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density # плотность жидкости
#
#     def edit_density(self, val): # изменение плотности
#          self._density = val
#
#     def calc_v(self, m): # вычесление объема жидкости в соответсвии заданой массе
#         res = m/self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v): # вычесление массы жидкости соответвующее заданному объему
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} составляет {res} kg')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} (плотность равна {self._density} kg/m^3),', end =" ")
#
# class Alcohol(Liqvid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength # крепость
#
#     def edit_strength(self, val): # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m): # переопределение вычесление объема жидкостиб соответсвующего заданного класса
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f"Объем алкоголя {m} kg {self._name} составляет {v_alc} m^3.")
#         return v, v_alc
#
#     def calc_m(self, v): # переопределение вычесление массы жидкости соответсвующего заданного класса
#         m = super().calc_m(v)
#         m_alc = v * self.strength
#         print(f"Вес алкоголя {v} kg {self._name} составляет {m_alc} m^3.")
#         return m, m_alc
#
#     def print_info(self):
#         super().print_info()
#         print(f"крепость = {self.strength:.0%}")
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(500)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(70)
# print(a.strength)
#
# a.print_info()


# class Liqvid: # жидкость
#     def __init__(self, name, density):
#         self._name = name
#         self._density = density # плотность жидкости
#
#     def edit_density(self, val): # изменение плотности
#          self._density = val
#
#     def calc_v(self, m): # вычесление объема жидкости в соответсвии заданой массе
#         res = m/self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v): # вычесление массы жидкости соответвующее заданному объему
#         res = v * self._density
#         print(f'Вес {v} m^3 {self._name} составляет {res} kg')
#         return res
#
#     def print_info(self):
#         print(f'Жидкость {self._name} (плотность равна {self._density} kg/m^3),', end =" ")
#
# class Alcohol(Liqvid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength # крепость
#
#     def edit_strength(self, val): # изменение крепости
#         self.strength = val
#
#     def calc_v(self, m): # переопределение вычесление объема жидкостиб соответсвующего заданного класса
#         v = super().calc_v(m)
#         v_alc = m * self.strength
#         print(f"Объем алкоголя {m} kg {self._name} составляет {v_alc} m^3.")
#         return v, v_alc
#
#     def calc_m(self, v): # переопределение вычесление массы жидкости соответсвующего заданного класса
#         m = super().calc_m(v)
#         m_alc = v * self.strength
#         print(f"Вес алкоголя {v} kg {self._name} составляет {m_alc} m^3.")
#         return m, m_alc
#
#     def print_info(self):
#         super().print_info()
#         print(f"крепость = {self.strength:.0%}")
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(500)
# a.calc_m(0.5)
#
# print(a.strength)
# a.edit_strength(70)
# print(a.strength)
#
# a.print_info()


class Liqvid: # жидкость
    def __init__(self, name, density):
        self.__name = name
        self.__density = density # плотность жидкости

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, chanage_name):
        self.__name = chanage_name

    @property
    def density(self):
        return self.__density

    @density.setter
    def density(self, value):
        self.__density = value

    def edit_density(self, val): # изменение плотности
         self.__density = val

    def calc_v(self, m): # вычесление объема жидкости в соответсвии заданой массе
        res = m/self.__density
        print(f"Объем {m} кг {self.__name} равен {res} m^3.")
        return res

    def calc_m(self, v): # вычесление массы жидкости соответвующее заданному объему
        res = v * self.__density
        print(f'Вес {v} m^3 {self.__name} составляет {res} kg')
        return res

    def print_info(self):
        print(f'Жидкость {self.__name} (плотность равна {self.__density} kg/m^3),', end =" ")

class Alcohol(Liqvid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength # крепость

    def edit_strength(self, val): # изменение крепости
        self.strength = val

    def calc_v(self, m): # переопределение вычесление объема жидкостиб соответсвующего заданного класса
        v = super().calc_v(m)
        v_alc = m * self.strength
        print(f"Объем алкоголя {m} kg {self.name} составляет {v_alc} m^3.")
        return v, v_alc

    def calc_m(self, v): # переопределение вычесление массы жидкости соответсвующего заданного класса
        m = super().calc_m(v)
        m_alc = v * self.strength
        print(f"Вес алкоголя {v} kg {self.name} составляет {m_alc} m^3.")
        return m, m_alc

    def print_info(self):
        super().print_info()
        print(f"крепость = {self.strength:.0%}")


a = Alcohol("Wine", 1064.2, 14)
a.print_info()

a.edit_density(1000)
a.print_info()

a.calc_v(500)
a.calc_m(0.5)

print(a.strength)
a.edit_strength(70)
print(a.strength)

a.print_info()

