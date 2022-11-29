# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

x = int(input("Введите первое целое число: "))
y = int(input("Введите второе целое число: "))

counter2 = 0
counter3 = 0
if x > y:
    print("Первое число должно быть меньше второго")
else:
    for number in range(x,y,):
        if (number % 2 == 0):
            counter2 += 1
        if (number % 3 == 0):
            counter3 += 1
    print(f"Чисел делящихся на 2 - {counter2}\nЧисел делящихся на 3 - {counter3}\nВсего в сумме - {counter2 + counter3}")

