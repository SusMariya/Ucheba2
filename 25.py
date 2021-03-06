from abc import ABC, abstractmethod

# class Currenty(ABC):
#     def __init__(self, value):
#         self.value=value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
# class Dollar(Currenty):
#     rate_to_rub = 74.16
#     suffix ="USD"
#
#     def convert_to_rub(self):
#         rub = self.value *Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
# class Euro(Currenty):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*"*50)
# for elem in d:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")
# print("*"*50)
# for elem in e:
#     elem.print_value()
#     print(f"= {elem.convert_to_rub():.2f} RUB")

# from abc import ABC, abstractmethod
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#         print("Display 1 Abctrakt metod")
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#         print("Display 2 Abctrakt metod")
#
# gc = GrandChild()
# gc.display2()
# gc.display1()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_matod(cls):
#         print("Я - метод внешнего класса")
#
#     def outer_obj_metod(self):
#         print("Я - являюсь связующим методом объекта внешнего класса")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_metod(self):
#             print("Я - метод внетреннего класса")
#             MyOuter.outer_class_matod()
#             print(MyOuter.age)
#             self.obj.outer_obj_metod()
#             print(self.obj.name)
#
#
#
# out = MyOuter("внешней")
# inner = out.MyInner("внетренний", out)
# inner.inner_metod()


# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.inter = self.Inter()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee List")
#         print('Name', self.name)
#
#     class Inter:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = '657'
#
#         def display(self):
#             print('Name', self.name)
#             print('Degree', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Alb9ina"
#             self.id = '007'
#
#         def display(self):
#             print('Name', self.name)
#             print('Degree', self.id)
#
# outer = Employee()
# outer.show()
#
# d1 = outer.inter
# d2 = outer.head
# d1.display()
# d2.display()

# class Geekforgeeks:
#     def __init__(self):
#            self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is the inner class in inner class")
#
# outer = Geekforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class OS:
#     def system(self):
#         return "Windows 10"
#
# class CPU:
#     def make(self):
#         return "Intel"
#
#     def model(self):
#         return "Core -i7"

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core -i7"
#
# comp = Computer()
# my_os = comp.os
# my_cpu=comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base Class")
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner  in SubClass")
#
# a = SubClass()
# a.display()
#
# # b= a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
# class Animal(Creature):
#     def slip(self):
#         print(self.name + "is sleeping")
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + "is playing")
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + "is barking")
#
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.slip()

# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса А")
#
# class D(B,C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
# d = D()

# class A:
#     def hi(self):
#         print("А")
#
# class B(A):
#     # def hi(self):
#     #     print("B")
#     pass
#
#
# class C(A):
#     # def hi(self):
#     #     print("C")
#     pass
#
# class D(B,C):
#      pass
#
# # d = D()
# # d.hi()
# print(D.mro())

class Point:
    def __init__(self, x=0, y=0):
        self.x= x
        self.y =y

    def __str__(self):
        return f"({self.x, self.y})"

class Styles:
    def __str__(self, color= "red", width = 1):
        print("Инициализатор Styles")
        self._color =color
        self._width =width

class Pos:
    def __init__(self, sp: Point, ep:Point, *args):
        print("Инициализатор Pos")
        self._sp= sp
        self._ep = ep
        Styles.__init__(self, *args)

class Line(Pos, Styles):
    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
l1.draw()