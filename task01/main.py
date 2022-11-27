# 1.	Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
# Примеры:
# o	5, 25 -> да
# o	4, 16 -> да
# o	25, 5 -> да
# o	8,9 -> нет

numberA = int(input("Введите первое число"))
numberB = int(input("Введите второе число"))

# if numberA / numberB == numberB:
#     print("Число A является квадратом числа B")
# elif numberB / numberA == numberA:
#     print("Число B является квадратом числа A")
# else:
#     print("Ни одно из чисел является квадратом другого")

if numberA ** 2 == numberB:
    print("да")
elif numberB ** 2 == numberA:
    print("да")
else:
    print("нет")

