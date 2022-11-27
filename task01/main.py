# 1.	Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# Примеры:
# o	5, 25 -> да
# o	4, 16 -> да
# o	25, 5 -> да
# o	8,9 -> нет

# numberA = int(input("Введите первое число"))
# numberB = int(input("Введите второе число"))

# if numberA / numberB == numberB:
#     print("Число A является квадратом числа B")
# elif numberB / numberA == numberA:
#     print("Число B является квадратом числа A")
# else:
#     print("Ни одно из чисел является квадратом другого")

# if numberA ** 2 == numberB:
#     print("да")
# elif numberB ** 2 == numberA:
#     print("да")
# else:
#     print("нет")

# Вариант: if numberA ** 2 == numberB or numberB ** 2 == numberA:


# 2.	Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# num = 0
# number = int(input("Введите число"))
# max = number
# while num < 4:
#     number = int(input("Введите число"))
#     if number > max:
#         max = number
#     num += 1
# print(max)

#Вариант решения:
# sp = list()
# for i in range(5):
#     n = int(input())
#     sp.append(n)
# print(max(sp))

#1.	Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# number_N = int(input("Введите число"))
# for i in range(-number_N, number_N + 1):
#     print(i, end=", ")

# 2.	Напишите программу, которая будет принимать на вход дробь и
# показывать первую цифру дробной части числа.

# number = float(input("Введите число"))
# # end_number = number * 10
# # print(int(end_number) % 10)
#
# #Вариант решения:
# print(int(number * 10) % 10)
# #Вариант решения2:
# number = input("Введите число").split(".")
# print(number[1][0])

#3.	Напишите программу, которая принимает на вход число и
# проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number = int(input("Введите число "))
# if number % 30 != 0 and (number % 10 == 0 or number % 15 == 0):
#     print("да")
# else:
#     print("нет")


# number = int(input("Введите число "))
# if number % 2 == 0:
#     print("да")
# else:
#     print("нет")


# number = int(input("Введите число "))
# print(int(number / 10) % 10)



