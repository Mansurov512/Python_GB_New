# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

number = int(input("Введите число: "))
isTrue = False

while number > 0:
    value1 = number % 10
    number //= 10
    value2 = number % 10
    if value1 > value2:
        isTrue = True
    else:
        isTrue = False
        break

print(isTrue)