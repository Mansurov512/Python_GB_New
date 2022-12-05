# 3.12 Вводим с клавиатуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и последней буквой "о" из исходной строки.
# Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

text = input("Введите строку: ")

firstLetterNumber = -1
lastLetterNumber = 0
amountLetter = 0
counter = 0

for char in text:
    if char == "о":
        amountLetter += 1 #считаем количество букв "о"
        lastLetterNumber = counter #каждый раз при нахождении будет записываться последний найденный номер
        if firstLetterNumber == -1: #-1 означает, что переменная не изменялась от начальных условий
            firstLetterNumber = counter #фиксируем номер первой буквы "о"
    counter += 1

if amountLetter <= 1:
    print("Буква \"о\" - одна или не встречается")
else:
    invertedText = ""
    print(text[firstLetterNumber + 1:lastLetterNumber]) #просто для наглядности показать что разворачиваем

    for i in text[firstLetterNumber + 1:lastLetterNumber]:  # переворачиваем отрезок текста в нужном диапазоне
        invertedText = i + invertedText

    print(invertedText)