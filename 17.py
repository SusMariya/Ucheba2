# список
# картеж
# словарь
#  множество

# s ="hello, WORLD! I am learning Python. 123!"
# print(id(s))
# # s = s.capitalize()
# print(s.capitalize()) # первый сивмол преобразуется в вверхний регистр, все остальные в преобразуетются в нижний регистр
# # print(id(s))
# print(s.lower()) # преобразует все символы в ниний регистр
# print(s.upper()) # преоразует все символы в верхний регистр
# print(s.swapcase()) # менят регистр симоволов на противоположный
# print(s.title()) # преобразует первые буквы всех слов в заглавные
# print(s.count("h")) # возвращает количество вхождений подстроки в строку
# print(s.count("he")) # возвращает количество вхождений подстроки в строку
# print(len(s))
# print(s.count("l", 8, 15)) #
# # print(s.find("Python", 3)) # возвращает первый индекс, который соответсвует элементу, начиная с начала строки
# print(s.index("Python")) # возвращает первый индекс, котррый соответсвует элементу, начиная с начала строки,
# # возвращает ValueError если совпадений не найдено
# print(s.index("cPython"))

# str1 = input("Введите два слова через пробел-> ")
# a = str1[str1.find(" ")+1:]
# b = str1[:str1.find(" ")]
# print(a)
# print(b)
# print(a+" "+b)

# t = 'ab12c59p7dq'
# digits = []
# for i in t:
#     if '1234567890'.find(i)!=-1:
#         digits.append(int(i))
# print(digits)
#
#
# num = "ab12c59p7dq"
# digits = []
# for i in num:
#     if 48 <= ord(i) <= 57:
#         digits.append(int(i))
# print(digits)
#
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     try:
#         digits.append(int(i))
#     except ValueError:
#         pass
# print('digits =', digits)


# y = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# u = y.index('(')
# h = y.index(')')
# l = y[u+1:h]
# print(l)
#
# s = "Дана ст(рока символов ,среди которых есть одна открыв)ающаяся"
# print(s[s.find('(') + 1:s.find(')')])

# h = 'aaaaaaaaaaaafaaaaaaaaaaaaaafaaaaaaaaaaaafffaaa'
# h1 = 'aaaaaaaaaaaafaaaaaaaaaaaaaafaaaaaaaaaaaafffaaa'
# if h.count('f') == 0:
#     pass
# elif h.count('f') == 1:
#     first = h.find('f')
#     print(first)
# else:
#     first = h.find('f')
#     second = h.rfind('f')
#     print(first, second)


# if h.count('f') == 1:
#     print(h.find('f'))
# elif h.count('f') >= 2:
#     print(h.find('f'), h.rfind('f'))

# s ="hello, WORLD! I am learning Python. 123@!"
# print(s.endswith("hello", 0, 5)) # определяет заканчивается ли строка заданной подстрокой

#
# print('abc123'.isalnum()) # определяет, состоит ли строка из букв и цифр
# print('ABAHGfjau'.isalnum()) # определяет, состоит ли строка из букв и цифр
# print('ABAHGDfjau@'.isalnum()) # определяет, состоит ли строка из букв? Не присутвует служебные символы
# print(''.isalnum()) # определяет, состоит ли строка из букв и цифр
# print('456258'.isdigit()) # определяет, состоит ли строка из цифр и проверка идет на число
# print('a-sd'.isidentifier()) # является ли строка интендификатором
# print('abc'.islower()) # определяет, являются ли буквенные символы строки строчными
# print(' '.isspace()) # определяет состоит ли стока только з пробельных символов
# print('\n'.isspace())
# print('\t \n'.isspace())
# print("Hello".istitle())# определяет начинается ли строка с заглавной буквы
# print("HELLO".isupper())# определяет состоит ли строка из заглавной буквы
# print('py'.center(10, "=")) # возвращает строку по центру
# print('     https://www.python.org/      '.lstrip()) # обрезает заданные символ с левой стророны, если символы не заданы
# print('     https://www.python.org/'.rstrip('org/')) # обрезает заданные символ с правой стророны, если символы не заданы
# print('https://www.python.org/'.lstrip('htps:/').rstrip('/')) # обрезает заданные символ  с левой и с правой стророны, если символы не заданы
# print('     https://www.python.org/     '.strip()) # обрезает заданные символ  с левой и с правой стророны, если символы не заданы


# s = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# print(s.replace("Nuthon", "Puthon")) # заменяет вхождение подстроки в строке


# stroka = "Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения"
# first = stroka.find("о")
# last = stroka.rfind("о")
# print(first, "", last)
# stroka = stroka[:first + 1] + stroka[first + 1:last].replace("о", "О") + stroka[last:]
# print(stroka)

# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s[:s.find('о') + 1] + s[s.find('о') + 1:s.rfind('о')].replace('о','О') + s[s.rfind('о'):])
# s= "-"
# seq = ("a", "b", "c")
# print(s.join(seq)) # объединили список в строку
# print("..".join(['1', '99']))

# print(":".join("Hello"))
# print(":".join(tuple("Hello")))

# print("Строка разделенная пробелами".split())
# print("Строка разделенная пробелами".split("а"))
# print('www.python.org'.split(".", 1))

# a = input("_> ").split()
# print(a)

# stroka = input("Введите ФИО - ")
#
# def ren(inp):
#     arr = inp.split(" ")
#     return arr[0] + " " + arr[1][0] + ". " + arr[2][0]+"."
#
# print(ren(stroka))

# stroka = input("Введите ФИО - ").split(" ")
# def ren(inp):
#     return inp[0] + " " + inp[1][0] + ". " + inp[2][0] + "."
# print(ren(stroka))


print('www.python.org'.rsplit(".", 1))