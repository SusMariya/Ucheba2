# os.path
import os.path

# print(os.path.split(r"C:\Users\suspi\PycharmProjects\pythonProject1\res_1.txt"))
# # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r"C:\Users\suspi\PycharmProjects\pythonProject1\res_1.txt"))
# # возаращает имя директории
# print(os.path.basename(r"C:\Users\suspi\PycharmProjects\pythonProject1\res_1.txt"))
# # возващает имя файла
# print(os.path.join(r"C:\Users", "suspi", "PycharmProjects", "pythonProject1"))
# # соединяет один или несколько компонентов пути с учетом особенностей OS

# dirs = [r"Work\F1", "Work\F2\F21"]
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     "Work": ['w.txt'],
#     r"Work\F1": ['F11.txt', 'F12.txt', 'F13.txt'],
#     r"Work\F2\F21": ['F211.txt', 'F212.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
# file_with_text = [r'Work\w.txt', r"Work\F1\F12.txt", r'Work\F2\F21\F211', r'Work\F2\F21\F212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху виниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown = topdown):
#         print(root)
#         print(dirs)
#         print(files)
#     print("-"*50)
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# print(os.path.exists(r'C:\Users\suspi\PycharmProjects\pythonProject1\last.txt'))
# # этот метод проверяет путь на существование (True - если путь существует)
#
# print(os.path.getctime(r'C:\Users\suspi\PycharmProjects\pythonProject1\one.txt')) # возвращает время создания файла
# print(os.path.getatime(r'C:\Users\suspi\PycharmProjects\pythonProject1\one.txt')) # возвращает время послденого доступа к файлу
# print(os.path.getmtime(r'C:\Users\suspi\PycharmProjects\pythonProject1\one.txt')) # возвращает время послденого изменения файла
# print(os.path.getsize(r'C:\Users\suspi\PycharmProjects\pythonProject1\one.txt')) # возвращает размер файла в байтах


import time
#
# path = r'C:\Users\suspi\OneDrive\Документы\учеба\Машины\2006-ISNOS_OMEGA_MO.pdf'
# size = os.path.getsize(path)
# kb = size//1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
# print("Размер: ", kb, "-KB")
# print('Дата последнего использования: ', time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print('Дата последнего редактирования: ', time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# print(os.path.normcase(r"C:\Users\suspi\OneDrive\Документы\учеба\Машины"))
# # нормализует регистр пути и слеши
# print(os.path.relpath(r'C:\Users\suspi\OneDrive\Документы\учеба\Машины/2006-ISNOS_OMEGA_MO.pdf'))
# # возвращает отосительный путь
# print(os.path.isfile(r'C:\Users\suspi\OneDrive\Документы\учеба\Машины/2006-ISNOS_OMEGA_MO.pdf'))
# # возвращает True, если конец пути является существующим файлом
# print(os.path.isdir(r'C:\Users\suspi\OneDrive\Документы\учеба\Машины/2006-ISNOS_OMEGA_MO.pdf'))
# # возвращает True, если конец пути является существующе директорией

# dir_name = "Work"
#
# objs = os.listdir(dir_name)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f'{obj} - dir')
#
#
# def print_tree(root):
#     for rot, dirs, files in os.walk(root, topdown=True):
#         if rot == root:
#             for i in dirs:
#                 print(i, "-dir")
#             for j in files:
#                 print(j, "-file",os.path.getsize(rot+"\\"+j), "byte")
# print_tree("Work")

# print("Hello")

print("вроде получилось создать")

print("Опять получилось)")