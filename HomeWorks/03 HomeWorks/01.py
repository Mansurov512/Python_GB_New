# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

num = int(input('Write number: '))
def to_hexadecimal(num):
    ans = ''
    while num > 0:
        help = num % 16
        if help == 10:
            help = "A"
        if help == 11:
            help = "B"
        if help == 12:
            help = "C"
        if help == 13:
            help = "D"
        if help == 14:
            help = "E"
        if help == 15:
            help = "F"

        ans = str(help) + ans
        num //= 16
    return ans

print(to_hexadecimal(num))
