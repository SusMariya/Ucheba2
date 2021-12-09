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

class Person:
    srill = 10 # квалификация сотрудника


    def print_info(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Данные сотрудника: {self.name} {self.surname}")

    def add_skill(self, k):
        self.srill += k
        print(f"квалификация сотрудника {self.name} {self.srill}", )


p1 =Person()
p1.print_info("Viktor", "Reznik")
p1.add_skill(3)
print()
p2 = Person()
p2.print_info("Anna", "Dolgova")
p2.add_skill(2)