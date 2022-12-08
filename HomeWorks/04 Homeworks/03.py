# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.

import random

numbers_list = []
lenth_list = 30 #количество элементов в списке

for i in range(0, lenth_list): #заполняем список случайными числами и выводим его в консоль
    numbers_list.append(random.randint(0, 200))
print(numbers_list)

for step in range(0, lenth_list):
    counter = 0
    number1 = numbers_list[0] #берём первый элемент списка
    number2 = 0
    value = len(numbers_list) - step - 1  #вывел в отдельную переменную для удобства отладки в дебаге
                                          # -step нужен чтобы не трогать уже отсортированные элементы
                                          # -1 нужен чтобы при втором проходе не сравнивало с уже отсортированным элементом
    for j in range(0, value):
        if (j + 1) < len(numbers_list): #проверка чтобы не выйти за максимальный индекс списка
            if number1 > numbers_list[j + 1]: #сравниваем первое число списка с каждым следующим
                number1 = numbers_list[j + 1] #если число меньше, то его и берём
                counter = j + 1 #записываем индекс нового минимального числа
    number2 = numbers_list.pop(counter) #извлекаем из неотсортированной части списка найденное минимальное значение
    numbers_list.append(number2) #добавляем его в конец списка

print(numbers_list) #уже отсортированный