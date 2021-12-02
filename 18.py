# import re

# s = "Я ищу совпадения в 2021 годую И я их наду в 2 счёта"
# reg = 'я'
# print(s.find(reg)) #15
# # find() - в cтроке будет искать шаблон и возвращать индекс
# # первого вхождения подстроки в строке если шаблон не найден будет возвращеть значение "-1"
# print(reg in s)
#
# print(re.findall(reg, s)) # возвращает список, содержащий все совпадения с регулярным выражением
# print(re.findall("12", s))
# print(re.search(reg, s)) # местоположение первого совпадения
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# # reg = 'Я'
# print(re.match(reg, s)) # поиск по заданному шаблону вначале строки
# reg = r"я"
# print(re.split(reg, s)) # возвращает список, в которой строка разбита по шаблону
# print(re.sub(reg, "!", s)) # заменяет совпадением указанным текстом


# s = "Я ищу совпадения в 2021 году. И я их наду в 2 счёта."
# reg = '[2021]'
# reg = '[12][09][0-9][0-9]'
# reg = '[А-Яа-яё]'
# reg = '[А-Яа-яё].'
# s = "Ели[-ели]."
# reg = r'[А-Яа-яё.\[\]-]'
#
# print(re.findall(reg, s))
#
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# # [^abc] # будет возвращать совпадения для любого символа кроме заданных (противоположные)
#
# t = "Час в 24-часовом формате от 00 до 23. 2021-06-15Е21:45. Минуты в диапазоне от 00 до 59. 2021-06-15Т01:09."
# reg = r'[0-9][0-9][\:][0-4][0-9]'
# print(re.findall(reg, t))
# reg = r'\d' # \d - одна цифра любая
# reg = r'\w' # \w буква, цифра, любой символ подчеркивания (_)
# reg = r'\s' # \s один пробельный символ (включая табуляцию и перенос строки)
# reg = r'\D' # \D все кроме цифр
# reg = r'\W' # \W все кроме буква, цифра, любой символ подчеркивания (_)
# reg = r'\S' # \S все кроме пробелов
# reg = r'\A' # \А ищет совпадения в начале строки
# reg = r'\Z' # \Z ищет совпадения в конце строки
# reg = r'\b' # \b ищет совпадения в начале или конце слова в зависимости от их расположения
# reg = r'\B'  #ищет совпадения не в начале и не конце


# s = "Я ищу совпадения в 2021 году. И я их наду в 2 счёта."
# reg = r'\w+' # количество повторений (+) - от 1 до бесконечности, (*) - от 0 до бесконечности, (?) - от 0 до 1
# reg = r'\d+' # возвращает числа целиком
# reg = r'\20*' #
# print(re.findall(reg, s))
#
# d = "Цифры:7, -17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))

# s = "05-03-1987 # Дата рождения"
# print("Дата рождения", re.sub("-", ".", re.sub("#.*", "", s)))

# s = "12 сентября 2021 года"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))
# print(re.findall(reg, s))
# s = "МИД - Министрество иностранных дел, ГЭС - гидроэлектростанция, ФСБ - Федеральная слуюба безопасности"
# reg = r'[А-ЯЁ]{2,}\s*[А-ЯЁ]'
# print(re.findall(reg, s))

#
# s = "+7 499 456-45-78, +74994564578, 7(499) 456 45 78, 74994564578"
# reg = r"[+][7]\d{10,}|[7]\d{10,}"
# print(re.findall(reg, s))


# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"[+-]?[0-9]{11,}"
# print(re.findall(reg, s))
#
#
# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7[0-9]{10}"
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 году. И я их наду в 2 счёта."
# reg = r'\w+\s\w+\.$'
# s = "45 78 456 78"
# reg = r'\d+\s+\d+$'
# s = "+7 908"
# reg = r'^\+\d+\s+\d+$'
# print(re.findall(reg, s))


# s = "Я ищу совпадения в 2021 году. И я их наду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s,
#                  re.IGNORECASE))  # или print(re.findall(reg, s, re.I)) или print(re.findall(reg, s, flags = re.I))
#
# print(re.findall(r'\d+', "12 + ۳"))
# print(re.findall(r'\d+', "12 + ۳ +п", flags=re.ASCII))

# re.DEBUG
# re.LOCALE
# re.DOTALL


# text = r'''
# Торт
# с вишней1
# вишней 2
# '''
# print(re.findall(r'Торт.с', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'^виш\w+', text, flags=re.MULTILINE))


# print(re.findall('''
#                 [\w.-]+
#                 @ # разбиваем по символу @
#                 [\w.-]+
#                 ''', "test@mail.ru", re.VERBOSE))

import re

# s = "author=Пушкин А.С.; title=Увгений Онегин; price=200; год=1830"
# reg = r'\w+\s*=\s*[^;]+'
# print(re.findall(reg, s))


# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
#
#
# print(validate_name('Python_master00053%/?'))
# print(validate_name('Python_master_master'))

# жадные (greedy) - захватывают максимально возможное число символов
#? ленивые (lazy) - захватывает минимальное возможное число символов

# *?, +?, ??
# {n, m}?, {, m}?, {n,}?
#
# text = "<body>Пример жадного соответствия регуляторных выражений</body>"
# # print(re.findall('<.*>', text))
# print(re.search('<.*?>', text).group())

# s = "<p>Изображение <img src='bg.jpg.> - фон страницы</p>"
# # reg = r"<img.*?>"
# reg = r'<img[^>]*>'
#


# text = "Уважаемые [12] коллеги! Направляем Вам[17]письмо-приглашение на Бетанкуровский [18]международный инженерный форум для Симочкина И.Ю.[20]"
# reg = r'\[.*?]'
# print(re.findall(reg, text))

# s = "Петр, Ольга, Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# s = "World2016, PS6, AI5, gdfg"
# reg = r'([a-z]+)(\d*)'
# print(re.findall(reg, s, re.I))
# print(re.search(reg, s, re.I).group())

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = input("Введите дату в формате dd-mm-YYYY: ")
# reg = r'([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2]])-([1][9][0-9][0-9]|[2][0][0-9][0-9])'
# print(re.findall(reg, s))
#
# IP 192.168.222.255
# s = '127.00.0.1'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "Базовый JS прост. Продвинутый Python сложен. Базовый Python прост."
# reg = r'[а-яё]+(?= Python)'
# reg = r'Базовый(?! Python)'
# reg = r'(?<=Базовый )\w{2,6}'
# reg = r'(?<!Продвинутый )Python'
# print(re.findall(reg, s, re.IGNORECASE))

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"
# reg = r'Людовик(?=VI)\w+'
# reg = r'Людовик(?!VI)\w+'
# reg = r'\w+(?<=Людовик)VI'
# reg = r'\w+(?<!Людовик)VI'
#
# print(re.findall(reg, s, re.IGNORECASE))

# s = "1X, Text ABC 123 A1B2C3"
# reg = r'(?<!\d)\d(?!\d)'
# print(re.findall(reg, s))
# s1 = "text from #START# till #END#"
# reg1 = r'(?<=#START#).*(?=#END#)'
# print(re.findall(reg1, s1))
# s2 = "12_34__56"
# reg2 = r'\d+(?=_(?!_))'
# print(re.findall(reg2, s2))

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s). group())
# m = re.search(reg, s)
# print("Строка: ", m[0])
# print("Цифра: ", m[1])
# print("Буква: ", m[2])


# s = "Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s)) # заменяем через индексы(скобки)

# s = "google.com and goodle.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

def is_roman_namber(num):
    patern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
    if re.search(patern, num):
        return True
    return False

print(is_roman_namber('MMDCCLXXIII'))
print(is_roman_namber('CCCMMVIIVV'))
print(is_roman_namber('DCLIII'))


