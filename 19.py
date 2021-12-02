# Рекурсия
# def elevator(n):
#     if n==0:
#         print("Вы в подвале")
#         return
#     print("-> ", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res +i
#     return res
#
# print((sum_list([1, 3, 5, 7, 9]))) # 25
#
# def sum_list(lst):
#     if len(lst) == 1: # Базовый случай
#         print(lst, "=> lst[0]: ", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]: ", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):
#     convert = "0123456789"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base] # 9 6 7
# #
#
# print(to_str(769, 10))  # 79 7


# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base] # F
#
#
# print(to_str(256, 16))  # F

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base] # F
#
#
# print(to_str(4, 2))

# names = ['Adam', ['Bob', ['Chet', 'Cat'], "Bard", "Bert"], "Alex", ['Bea', 'Bill'], 'Anna']
# def count_items(item_list):
#     count =0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
# print(count_items(names))

# print(type(names[0]) == list)
# print(names[0])


# names = ['Adam', ['Bob', ['Chet', 'Cat'], "Bard", "Bert"], "Alex", ['Bea', 'Bill'], 'Anna']
# def count_items(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count
# print(count_items(names))

#
# def union(s):
#     if not s:  # s==[]
#         return s
#     if isinstance(s[0], list):
#         return union(s[0] + union(s[1:]))
#     return s[:1] + union(s[1:])
# names = ['Adam', ['Bob', ['Chet', 'Cat'], "Bard", "Bert"], "Alex", ['Bea', 'Bill'], 'Anna']
# print(union(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] =="\t" or text[0] ==" ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
# print(remove(" Hello \tWorld Hi "))

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos = pos +1
#     return found
#
# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))


# def seq_search(s, item): # вариатн 2
#     for i in s:
#         if i == item:
#             return True
#     else:
#         return False

# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[stop] >item:
#                 stop = True
#             else:
#                 pos = pos +1
#     return found
#
# lst = [0, 1, 2,  8, 13, 17, 19, 32,42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

def binary_search(s, item):
    first = 0
    last = len(s)-1
    found = False

    while first <= last and not found:
        midlpoint = (first + last)//2
        if s[midlpoint] == item:
            found = True
        else:
            if item <=s[midlpoint]:
                last = midlpoint-1
            else:
                first = midlpoint+1
    return found


lst = [0, 1, 2,  8, 13, 17, 19, 32,42]
# print(binary_search(lst, 3))
print(binary_search(lst, 2))