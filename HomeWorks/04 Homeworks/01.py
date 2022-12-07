# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

numbers_list = []

for i in range(0, 10): #заполняем список случайными числами и выводим его в консоль
    numbers_list.append(random.randint(0, 10))
print(numbers_list)

numbers_list_sum = 0

print("", end = "    " ) #для удобства форматирования вывода на консоль
for j in range(1, int(len(numbers_list)), 2): #выводим числа на нечётных позициях и суммируем каждое
    print(numbers_list[j], end = "     " )
    numbers_list_sum += numbers_list[j]

print(f"\nСумма чисел на нечётных позициях: {numbers_list_sum}")