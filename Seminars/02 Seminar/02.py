# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.


def count_letters(txt: str):
    txt = txt.strip()
    count_vowels = 0
    count_consonants = 0

    for i in 'a', 'o', 'i', 'u', 'e':
        count_vowels += txt.count(i)

    count_consonants = len(txt) - count_vowels

    print('vowels = ', count_vowels)
    print('consonants = ', count_consonants)

s = input('Enter text: ')

count_letters(s)
