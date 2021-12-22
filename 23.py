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

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}" # или return str(self.x)
class Prop:
    def __init__(self, sp: Point, ep:Point, color:str = "red", width: int= 1):
        print("Инициализатор базового класа Prop")
        self.sp = sp
        self.ep = ep
        self.color = color
        self.__width = width

    def get_width(self):
        return self.__width

class Line(Prop):
    def __init__(self, *args):
        print("Переопределенный инициализатор Line")
        # Prop.__init__(self, *args) # или так как ниже
        super().__init__( *args)
        self.__width = 5

    def draw_line(self):
        print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")

class Rect(Prop):
    def draw_Rect(self):
        print(f"Рисование прямоугольника: {self.sp}, {self.ep}, {self.color}, {self.__width}")

line = Line(Point(1, 2), Point(10, 20))
print(line.__dict__)
# print(Line.width)
# Line.width = 10
# print(Line.width)
line.draw_line()
# Line = Rect(Point(38, 40), Point(10, 20))
# Line.draw_Rect()