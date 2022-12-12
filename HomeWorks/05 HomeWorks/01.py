# # Сделать игру морской бой
# # Как я понял, как минимум с полем 3х3 и однопалубным кораблём.
#
# ТЗ самому себе для понимания что делать:
# Сделать какое-то поле 3х3, заполнив его нулями или какими-то символами
#
# Рандомайзером сделать одно поле единичкой
# или
# Рандомайзером сделать координаты одного поля, например двумя переменными
# И если введённые координаты совпали, то выводить сообщение.
# Так же нужно у поля чтобы была координатная сетка.
# Нужно вводить координаты удара.
# После ввода удара, поле должно переотрисовываться с учётом попадания.

field = []
fieldsize = 3
empty_line0 = ["■ "] * fieldsize# я хотел в начале использовать лишь один список и им заполнять все строки игрового поля,
empty_line1 = ["■ "] * fieldsize# но ссылочный тип данных испортил мою идею, а победить я его не смог,
empty_line2 = ["■ "] * fieldsize# чтобы он стал действительным. Так бы можно было бы масштабировать поле.

# for r in range(fieldsize): # заполняем пустое поле
#     field.append(empty_line)

field = [empty_line0, empty_line1, empty_line2] # заполняем пустое поле

def print_field(): #распечатка поля в консоль с нумерацией строк и столбцов
    print("  ", end="")
    for k in range(fieldsize):
        print(f"{k+1}", end="  ")
    print()
    for i in range(fieldsize):  # выводим в консоль пустое поле
        print(f"{i + 1}", end=" ")
        for j in range(fieldsize):
            print(field[i][j], end=" ")
        print()

print_field()

import random
x_coordinate_ship = random.randint(0, fieldsize) + 1# координаты корабля компьютера
y_coordinate_ship = random.randint(0, fieldsize) + 1

x_coordinate_strike = 0
y_coordinate_strike = 0

while x_coordinate_ship != x_coordinate_strike and y_coordinate_ship != y_coordinate_strike: # цикл самой игры
    x_coordinate_strike = int(input(f"Введите координату по ширине поля(строку) от 1 до {fieldsize} включительно: "))# координаты удара
    y_coordinate_strike = int(input(f"Введите координату по высоте поля(столбец) от 1 до {fieldsize} включительно: "))

    if x_coordinate_ship != x_coordinate_strike and y_coordinate_ship != y_coordinate_strike:
        field[x_coordinate_strike - 1][y_coordinate_strike - 1] = "O "
        print_field()
        print("Мимо!")
        print()
else:
    field[x_coordinate_strike - 1][y_coordinate_strike - 1] = "X "
    print_field()
    print("Вы попали и выиграли!")