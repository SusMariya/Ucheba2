# создание модулей

# import math
# print(math.pi)
#
# from math import pi
# print(pi)

## import пакет.модуль
# import geometry.rect
# import geometry.sq
# import geometry.trian
# r1 = geometry.rect.Rectangle(1, 2)
# r2 = geometry.rect.Rectangle(3, 4)
#
# s1 = geometry.sq.Square(10)
# s2 = geometry.sq.Square(20)
#
# t1 = geometry.trian.Triangl(1, 2, 3)
# t2 = geometry.trian.Triangl(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# или
# #
# from giometry import rect, sq, trian
#
# if __name__ == "__main__":
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangl(1, 2, 3)
#     t2 = trian.Triangl(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
# if __name__ == "__main__":
#     main()

# Или

# from geometry import * # это когда rect, sq и trian в __init__.ry
# #
# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangl(1, 2, 3)
# t2 = trian.Triangl(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# from car import elecarclass
#
# def main():
#     e = elecarclass.ElectroCar("Tesla", 'T', 2018, 99000)
#     e.show_car()
#     e.description_batarry()
# if __name__ =="__main__":
#     main()

