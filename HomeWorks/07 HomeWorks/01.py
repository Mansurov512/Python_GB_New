# Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
# Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.), бесконечный цикл, функции и прочий функционал.

# Программа будет, как консольный бот, который будет нас спрашивать,
# что и как нужно сделать - вывести, показать, перезаписать, добавить событие в определенный день недели.
#
# Сделать календарь рабочий на пол ставки, рабочие дни с понедельника по пятницу, рабочее время с 10:00 до 14:00.
# На одну неделю сделаю.
# День недели
# Время с промежутком в 1 час
# Всё это можно просто сделать по ключу цифрами
# И нужен ввод самого задания/описания текстом
# Предусмотреть вывод на консоль хотя бы просто одного дня недели
# Вывод целой недели тоже бы нужно, но в одну строчку будет сложно с аккуратным форматированием,
# так как у комментариев будет разная длина количества символов.
# Потому вывод проще сделать построчно
#
# Работа программы в бесконечном цикле пока не будет введена команда на закрытие, хотя это уже доп функционал.
#
# Ещё нужно удалять события или изменять их
#
# working_days = ["Monday", "Tuersday", "Wendsday", "Thursday", "Friday"]
lines_file = []
day = {1: "Monday", 2: "Tuersday", 3: "Wendsday", 4: "Thursday", 5: "Friday"}
time = {1: "10:00-11:00", 2: "11:00-12:00", 3: "12:00-13:00", 4: "13:00-14:00"}
actions_schedule = {"add": 1, "show": 2, "del": 3}

while True:
    action = input("add - добавить новую задачу\n"
                   "show - показать расписание дня недели\n"
                   "del - удалить задачу\n"
                   "Введите что хотите сделать: ")

    if actions_schedule[action] == 1:

        day_number = int(input("Введите номер дня недели от 1 до 5: "))
        file_name = day[day_number] + ".txt"

        with open(file_name, "r", encoding="utf-8") as file:  # считываем содержимое файла в список
            lines_file = file.readlines()

        day_time = int(input("Введите порядковый номер необходимого времени от 1 до 4, в котором:\n"
                             "1 - 10:00-11:00\n"
                             "2 - 11:00-12:00\n"
                             "3 - 12:00-13:00\n"
                             "4 - 13:00-14:00\n"))

        task = input("Введите рабочую задачу для указанного времени: ")

        with open(file_name, "w",
                  encoding="utf-8") as file:  # перезаписываем новое задание на строчку соответствующее порядковому номеру времени
            # при этом сохраняя все предыдущие записи на остальных строчках
            for i in range(1, 5):
                if i != day_time:
                    file.writelines(lines_file[i - 1])
                else:
                    file.writelines(day[day_number])
                    file.writelines(", ")
                    file.writelines(time[day_time])
                    file.writelines(" - ")
                    file.writelines(task)
                    file.writelines("\n")

    if actions_schedule[action] == 2:
        day_number = int(input("Введите номер дня недели от 1 до 5: "))
        file_name = day[day_number] + ".txt"

        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

    if actions_schedule[action] == 3:
        day_number = int(input("Введите номер дня недели от 1 до 5: "))
        file_name = day[day_number] + ".txt"

        with open(file_name, "r", encoding="utf-8") as file:  # считываем содержимое файла в список
            lines_file = file.readlines()

        day_time = int(input("Введите порядковый номер необходимого времени от 1 до 4, в котором:\n"
                             "1 - 10:00-11:00\n"
                             "2 - 11:00-12:00\n"
                             "3 - 12:00-13:00\n"
                             "4 - 13:00-14:00\n"))

        with open(file_name, "w",
                  encoding="utf-8") as file:  # перезаписываем новое задание на строчку соответствующее порядковому номеру времени
            # при этом сохраняя все предыдущие записи на остальных строчках
            for i in range(1, 5):
                if i != day_time:
                    file.writelines(lines_file[i - 1])
                else:
                    file.writelines(" \n")

        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)

