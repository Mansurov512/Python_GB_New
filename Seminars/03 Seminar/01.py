# 1) Есть список:  s = ['a', 'b', 'c', 'd', 'e']
# Необходимо написать программу, которая сдвинет список spisok следующим образом: ['c', 'd', 'e', 'a', 'b']

s = ['a', 'b', 'c', 'd', 'e']
a, b = s.pop(0), s.pop(0)
s.append(a)
s.append(b)
print(s)
