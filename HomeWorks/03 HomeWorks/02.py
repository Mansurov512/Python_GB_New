# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

# Я так понимаю, что используя try catch конструкцию можно было бы попробовать преобразовать число во float
# и если не получается, то значит строка не дробное число. Но пока что мы это не проходили по курсу,
# потому решу другим образом

text = input("Введите строку: ")

countCommaOrDot = 0
numberPosition = 0

for char in text:
    if char == "." or char == ",":
        countCommaOrDot += 1 #считаем количесто запятых и/или точек в строке
    if countCommaOrDot == 0:
        numberPosition += 1 #высчитываем номер индекса точки или запятой

withoutDotOrComma = ""

if countCommaOrDot != 1:#если в строке нет точки/запятой или их больше 1 то это уже точно не дробное число
    print("Просто какая-то строка.")#сделал отдельный if чтобы остальной код не выполнялся тогда
else:
    withoutDotOrComma = text[0:numberPosition] + text[numberPosition + 1:len(text)] #пересклеиваем сроку без найденной точки или запятой
    if withoutDotOrComma.isdecimal(): #проверяем все ли символы десятичные знаки
        print("Строка является числом дробным.")
    else:
        print("Просто какая-то строка.")
