# Задайте список из нескольких чисел.Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# sum = 0
# for i in range(len(lst)):
#    if i % 2 == 1:
#        sum += lst[i]
# print(f"Сумма равна: {sum}")

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# from random import randint
# array_size = int(input("введите количество элементов в списке: "))
# lst1 = []
# for i in range(array_size):
#    lst1.append(randint(1, 10))
# print(lst1)
# lst_mulriplied = []
# ln = len(lst1)
# for i in range(ln):
#    if i >= ln/2:
#        break
#    print(lst1[i] * lst1[-i-1], end=' ')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
print(lst)
new_lst = [round(i % 1,2) for i in lst if i % 1 != 0]
print(f"разница макс и мин: {max(new_lst) - min(new_lst)}")