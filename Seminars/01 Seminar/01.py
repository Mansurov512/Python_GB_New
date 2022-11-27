number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
if number1 == number2 == 1 or number1 == number2 == 0:
  print('оба числа являются квадратами друг друга')
elif number1 == number2 ** 2:
  print("первое число является квадратом второго!")
elif number2 == number1 ** 2:
  print("второе число являестя кватратом первого")
else:
  print("числа не являются кватратом друг друга")
