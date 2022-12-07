import random
linemas = []
mas = []

for i in range(3):
    #linemas = []    #я так и не понял почему, но если написать в этом месте linemas.clear() вместо linemas = [] то очищается и уже добавленный список
    linemas.clear() #linemas внутри mas, будто это ссылочный тип данных. Потому каждый раз приходится объявлять пустой список
                    #при этом ещё и заполняет у итогового списка все внутренние списки последним набором из списка linemas
    print(mas)
    print(linemas)

    for j in range(3):
        linemas.append(random.randint(0, 10))
    print(linemas)
    mas.append(linemas)
    print(mas)

# for k in mas:
#     for i2 in k:
#         print(i2, end='  ')
#     print()


# import random
# linemas = []
#
# for j in range(4):
#     linemas.append(random.randint(0, 10))
# print(linemas)
#
# mas = []
# for i in range(3):
#     mas.append(linemas)
#     #mas[i] = [0, 1, 2]
# print(mas) # Выведет [[0, 0, 0], [0, 0, 0], [0, 0, 0]]