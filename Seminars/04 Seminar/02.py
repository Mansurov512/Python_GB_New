#Сделать основу игры морской бой.

field_player = []
field_computer = []

i = 0
j = 0

while i < 10:
    line_computer = []
    k = 0
    while k < 10:
        line_computer.append('_')
        k += 1
    field_computer.append(line_computer)
    i += 1

while j < 10:
    print(field_computer[j])
    j += 1