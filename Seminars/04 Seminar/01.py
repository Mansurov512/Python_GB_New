# Игра "Камень-Ножницы-Бумага"

player_step = input("Введите К - Камень, Н - Ножницы, Б - Бумага: ")

import random

computer_step = random.randint(0, 2)
if (computer_step == 0 and player_step == "Н") or (computer_step == 1 and player_step == "Б") or (computer_step == 2 and player_step == "К"):
    print("Компьютер выиграл.")
if (computer_step == 0 and player_step == "Б") or (computer_step == 1 and player_step == "К") or (computer_step == 2 and player_step == "Н"):
    print("Вы выиграли!")
if (computer_step == 0 and player_step == "К") or (computer_step == 1 and player_step == "Н") or (computer_step == 2 and player_step == "Б"):
    print("Ничья.")


# 0 - Камень, 1 - Ножницы, 2 - Бумага