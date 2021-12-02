import random as r


# def buble(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1]= array[j + 1], array[j]
#         # print(array)
#         # print("-" * 40)
#
# a = [r.randint(1, 99) for i in range(10)]
# print(a)
# buble(a)
# print(a)

# a = [5, 9, 6, 7]
# b = [3,  11, 8]
# c = [2, 4]
# d = [10, 1, 12]
# f1 = a+b+c+d
# # print(f1)
# t = input("Выбирете тип сортировки (1 - по убывванию, 2 - по возрастанию): ")
#
# def buble(f):
#     for i in range(len(f) - 1):
#         for j in range(len(f)-i-1):
#             if t ==str(1):
#                if f[j] > f[j + 1]:
#                 f[j], f[j + 1]= f[j + 1], f[j]
#             elif t ==str(2):
#                 if f[j] < f[j + 1]:
#                     f[j], f[j + 1] = f[j + 1], f[j]
#             else:
#                 return
# print("такой сортировки нет")
# print(f1)
# buble(f1)
# print(f1)

#
# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     # print("l", l)
#     # print("r", r)
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)

# def shell_sort(s):
#     gap = len(s)
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, "Список: ", s)
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)
#
# f = open(r"C:\Users\suspi\PycharmProjects\pythonProject1\text.txt", "r")
# print(f.read(3))
# print(f.read())
#
# f.close()

# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(*f)
# print(f)
#
# f = open("text1.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open("text1.txt", "r")
# print(f.rereadline())
# print(f.rereadline(8))
# print(f.rereadline())

# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
# # for line in f:
# #     print(line)
# f.close()

# f = open('xyz.txt', 'w') # записали новый документ
# f.write('Hello \nWolrd')
# f.close()
#
# f = open('xyz.txt', 'a') # дописали в конец файла
# print(f.write('New text'))
# f.close()

# f = open('xyz.txt', 'a') # дописали в конец файла
# # print(f.write('New text'))
# lst = [str(i) + str(i -1) for i in range(1, 20)]
# print(lst)
# # line = ['This is line 1', 'This is line 2']
# # f.writelines(line)
# for index in lst:
#     f.write(index + '\t' + '\n')
#
# f.close()

# f = open('text2.txt', 'r', encoding='utf - 8')
# lst = f.readline()
# print(lst)
# # lst[1] = "Hello wolrd\n"
# for i in range(len(lst)):
#     if lst[i] == 'изменить строку в списке;':
#         lst[i] == 'Hello wolrd;\n'
# print(lst)
# f.close()
# f = open('text2.txt', 'w', encoding='utf - 8')
# f.writelines(lst)
# f.close()

# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# my_file.close()
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

########################### 30.11.2021
# f = open('text.txt', 'w')
# f.write('Hello!')
# f.close()
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell()) # 3 номер где стоит курсор
# print(f.seek(1)) # 1
# print(f.read())
# f = open('text.txt', 'r+')
# print(f.write('I am learning Python'))
# print(f.seek(3))
# print(f.write('-new string-'))
# print(f.tell())
#
# f.close()
#
# with open("text.txt", 'w+') as f:
#     print(f.write('0123456789\nlkpojinjnk'))
#
# with open('text.txt', 'r') as f:
#     for line in f:
#         print(line[:5])

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return "\t ".join(lt)
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print('Doone!')

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# def get_line(lt):
#     lt = list(map(str, lt))
#     return "\t ".join(lt)
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print(lst)
# print(len(lst))

# file_name = 'res_1.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
# with open(file_name, 'r') as f:
#     file_lst = f.read().split(' ')
#
# file_lst = list(map(float, file_lst))
# print(file_lst)
# print(len(file_lst))

# file_name = 'res_2.txt'
# lst = ['методами', 'символов', 'попыткой']
# def get_line(lt):
#     lt = list(map(str, lt))
#     return "\t ".join(lt)
# with open(file_name, 'w') as f:
#         f.write(get_line(lst))
#         bast = 0
#         for i in range(len(lst)):
#             if len(lst[i]) > len(lst[bast]):
#                 bast = i
#         print(lst[bast])
#
# print(lst)

# with open('text1.txt', 'r') as f:
#     lst = f.read().split()
#     print(lst)
#     m = max(len(i) for i in lst)
#     print([i for i in lst if len(i) == m])

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
#
# with open("one.txt", 'w') as f:
#     f.write(text)
#
# read_txt = "one.txt"
# write_txt = 'two.txt'
# with open(read_txt, 'r') as fr, open(write_txt, "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)
#
# with open(write_txt, 'r') as fr:
#     for line in fr:
#         print(line, end ="")


import os
#
# print("текущая дирктория", os.getcwd())  # возвращает текущую дерикторию (там где *.py)
# print(os.listdir("..")) # возвращает список дерикторий и фалов, находящихся в текущей директории (по умлочанию) или в директории указанного пути
# os.mkdir("Free") # создает директорию по указанному пути
# os.mkdir("Free.free1")
# os.makedirs("Free/free1/free2") # создаст конечную директорию и промежуточные папки если их не существует
# os.makedirs("Free/free1/free2/free4") # создаст конечную и так же промежуточные директорию и промежуточные папки если их не существует
# os.remove("xyz.txt") # удаляет файл
# os.rename("free", "test") # переименовать файл или папку
# os.rename("two_new.txt", "Free.free1/two_new.txt") # переименовать файл или папку
# os.renames("text1.txt", "text/new_text.tx.txt") # переименовывает и перемещает файл, создавая промежуточные директории, если их нет

# os.rmdir("Free.free1") # удаляет пустую директорию (папка). Если директория не пустая  - будет ошибка
# возвращает имена объектов в дереве директорий, обходя это дерево сверху вниз topdown=True или снизу вверх topdown=Fals
# for root, dirs, file in os.walk("text", topdown=False):
#     print("Root: ", root)
#     print("Subdirs: ", dirs)
#     print("Files: ", file)

# for root, dirs, files in os.walk("Work", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)

for root, dirs, files in os.walk("Work", topdown=True):
    if not os.listdir(root):
        os.rmdir(root)
        print(f"Директория {root} удалена")
