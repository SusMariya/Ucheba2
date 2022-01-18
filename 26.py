# class Displayer:
#     @staticmethod
#     def display(massage):
#         print(massage)
#
# class LoggerMixin:
#     def log(self, massage, filename = 'logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(massage)
#
#     def display(self, massage):
#         Displayer.display(massage)
#         self.log(massage)
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, massage, filename = ''):
#         super().log(massage, filename="subclasslog.txt")
#
# sub = MySubClass()
# sub.display("Это строка будет отображаться и регистрироваться записываться в файл")



# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Inin print")
#         self. name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID +=1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
# class NoteBook(Goods, MixinLog):
#     pass
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# n2 = NoteBook("HP", 1.5, 35000)
# n2.save_sell_log()


class Clock:
    __DAY = 86400 # 24*60*60 число секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("секунды должны быть целым числом")

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60 # секунды
        m = (self.__secs // 60) % 60 # минуты
        h = (self.__secs // 3600) % 24 # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        return Clock(self.__secs + other.__secs)

    def __isub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        return Clock(self.__secs - other.__secs)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        return Clock(self.__secs * other.__secs)

    def __truediv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

        return Clock(self.__secs // other.__secs)

    def __imod_(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.__secs %= other.__secs
        return Clock(self.__secs)

    def __eq__(self, other):
        return self.__secs == other.__secs
        #     return True
        # return False
    def __ne__(self, other):
        return self.__secs !=other.__secs
        # return not self.__eq__(other)

# c1 = Clock(100)
# c2 = Clock(200)
# # print(type(c1))
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2
# print(c3.get_format_time())
# c4 = c1 + c2 + c3
# print(c4.get_format_time())

c1 = Clock(100)
c2 = Clock(100)
c3 = Clock(300)
# c1 +=c2 + c3
print(c1.get_format_time())
print(c2.get_format_time())
print(c3.get_format_time())
# # c1-=c2
# print("c1-=c2", c1.get_format_time())
# c4=c1*c2
# print("c1*c2", c4.get_format_time())
# c4 = c1/c2
# print("c1//c2", c4.get_format_time())
# c1%=c2
# print("c1%c2", c1.get_format_time())

if c1 == c2:
    print("Время одинаково")
if c1 != c3:
    print("Время разное")

