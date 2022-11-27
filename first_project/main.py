# a = 5
# b = "string"
# c = 0.5
# t = True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(t))

# for i in range(5):
#     print("python")

# i = 0
# while i < 3:
#     print("python")
#     i += 1 # также можно умножить, вычесть, разделить: -=, *=, /=

# n = 567
# print(n // 10)
# print(n % 10)

# sp = []
# sp.append(2)
# sp.append(9)
# print(sp)

sp = [1, 2, 3, 5]
# print(sp[2])
# print(sp[-1]) # вывод последнего элемента в списке (нумерация с конца: -1, -2 и т.д.)

for i in range(0, len(sp)):
    # print(sp[i])
    print(sp[i], end=" ") # вывод по индексам в списке (если что-то меняется, то исп. этот способ)

for el in sp:
    print(el, end=" ") # вывод по элементам

print(*sp) # без (*) выводит в кв.скобках, со (*) без них

