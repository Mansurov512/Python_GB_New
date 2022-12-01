# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

x = int(input("Введите количество чисел: "))

i = 0
numbersList = []

while i < x:
    number = int(input(f"Введите число номер {i+1} из {x} чисел: "))
    numbersList.append(number)
    i += 1

numberMax = numbersList[0] #изначально переменные равны первому числу в списке чисел
numberLessMax = numbersList[0]

j = 0

while j < len(numbersList):
    if numbersList[j] > numberMax:
        numberLessMax = numberMax #присваиваем бывшее максимальное значение
        numberMax = numbersList[j] #обновляем новое максимальное значение
    j += 1

print(f"В списке самое большое число {numberMax}, а второе максимальное {numberLessMax}.")

# for n in numbersList:
#     if n > numberMax:
#         numberLessMax = numberMax #присваиваем бывшее максимальное значение
#         numberMax = n #обновляем новое максимальное значение
#         print(f"В списке самое большое число {numberMax}, а второе максимальное {numberLessMax}.")


