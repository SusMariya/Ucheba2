# a=15.606996595955297846948
# print(a)
# print(type(a))
#
# print(6/2)
# print(7/2)
# print(7//2)
#
# a=5
# b=7
# c=3
# print("сумма:", a+b+c)
# print("произведение:", a*b*c)
# print("среднеарифиметическое:", (a+b+c)/3)

# namber = 6+4*5**2+7
# print(namber)

# num = 10
# num +=5 #num = num+5
# print(num)

# a = 9753
# print("Исходное число:", a)
# b = a%10
# c = (a//10)%10
# d = (a//100)%10
# f = (a//1000)%10
#
# print("Обратное число: ", b, c, d, f)
# num = 9753
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# # print("num", num)
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
#
# print(int(num1) +num2)
# print(num1 +str(num2))
#

# print(int(3.8)) # 3
# print(round(3.895, 2)) # 4

# a= 5/3
# print(a)
# print(round(a, 2))

# a = "5.2"
# b = 10
# print(float(a)+b)

# a = 1
# b = 2
# print("a:", a, "b:", b)

name = "Victor"
age = 28
grade = 9.2
#print("Меня зовут "+ name+ ". Мне "+ str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end=" ")
# print("Я учу Питон")
# print("It`s %s, %d. Level: %.2f" % (name, age, grade))
#
# print("This is a {1}. It s {0}.".format("ball", "red"))

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}. Ваш город {1}".format(name, city))

# name = input("Введите число: ")
# city = input("Введите степень: ")
# # print("Вас зовут {0}. Ваш город {1}".format(name, city))
# print("в сетпени", name**city)

# a = input("Введите 1 число: ")
# b = input("Введите 2 число: ")
# c = input("Введите 3 число: ")
# f = input("Введите 4 число: ")
# sum1 = float(a)+float(b)
# sum2 = float(c)+float(f)
# # sum = float(a+b)/float(c+f) ## или так
# # sum = int(a+b)/int(c+f) ## или так
# print(round(sum1/sum2, 2))

# a = int(input("Введите 1 число: "))
# b = int(input("Введите 2 число: "))
# c = int(input("Введите 3 число: "))
# f = int(input("Введите 4 число: "))
# sum = (a+b)/(c+f) ## или так
# print(round(sum))

# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
#
# print(bool("Python")) # True
# print(bool("")) # False
# print(bool(" ")) # True
# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(51)) # True
# print(bool(-51)) # True
# print(bool(-5.1)) # True
# print(bool(False)) # True
# print(bool(None)) # True #истину дает нам все что угодно кроме ""(пустая строка без пробела), 0, False, None


# test = None
# print(test)
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# print("привет">"Привет")
#
# print(2 < 4 < 9)
# print(2*5 > 7 >= 4+3)
# print(3*3 <= 7 >= 2)
# a = 10
# b = 5
# c = a ==b
# print(a, b, c)

# print(5-3 == 2 and 1+2 == 4)
#
# print(4-2 == 2 or 1+3 == 4)
#
# print(not 9-9)

# v1 = (0 or 1) and (0 or 1)
# v2 = 0 or 1 and 0 or 1
# print(v1)
# print(v2)
# a=b=0
# v3 = (a or 1) or (b and 0)
# print(v3)

# if логическое выражение:
#     выражение
# cnt = 15
# if cnt <10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите взраст: "))
# if age >= 18:
#     print("Достпу на сайт разрешен")
# else:
#     print("Достпу на сайт заперщен")

# a =15
# b = 5
# if a>b:
#     print("a>b")
# elif a<b:
#     print("b>a")
# else:
#     print("b==a")

a = int(input("Введите первую сторну: "))
b = int(input("Введите вторую сторну: "))
c = int(input("Введите третью сторну: "))
if a == b == c:
    print("Треугольник равносторнний")
elif a == b or b == c or a == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")

