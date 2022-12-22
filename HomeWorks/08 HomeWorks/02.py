# 2) Нужно написать программу.
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, a так же студентов, у которых низкие оценки.

# Мои мысли:
# Низкие оценки - например у кого средний бал меньше чем 4
#
# Класс студент пусть будет просто нумерация
#
# Генератором случайных чисел думаю сделать список оценок progress.
# Сделать наверное через метод в самом классе
# Нужно как-то сортировку объектов сделать по их атрибутам

import random

class Student:
    def __init__(self, name, group): # у каждого экземпляра задаётся имя и номер группы
        self.name = name
        self.group = group

    def get_name(self):
        return self.name

    def get_group(self):
        return self.group

    def get_progress(self): # генерируем список из 5-ти оценок от 2 до 5.
        progress_list = []
        for i in range(5):
            progress_list.append(random.randint(2, 5))
        return progress_list

Student01 = Student("Andrey", 1166) # создаём 6 объектов класса "Student" и каждому задаём атрибуты
Student02 = Student("Mark", 1166)
Student03 = Student("Anna", 1166)
Student04 = Student("Misha", 3056)
Student05 = Student("Sam", 3056)
Student06 = Student("Lia", 3056)

def sorted_students_names(): # вывод сортированного списка имён студентов
    names = []
    names.append(Student01.get_name()) # выглядет очень топорно, но как ещё перечислить 6 экземпляров - не знаю
    names.append(Student02.get_name())
    names.append(Student03.get_name())
    names.append(Student04.get_name())
    names.append(Student05.get_name())
    names.append(Student06.get_name())
    names.sort() # так как ДЗ на классы и ООП, я так понял что можно использовать встроенную функцию, а не реализовывать её
    return names

def bad_grades_students_list(name01, name02, name03, name04, name05, name06,            # вводим имена и список оценок для каждого студента
                             grades01, grades02, grades03, grades04, grades05, grades06,
                             ):

    bad_grades_students_list = []

    def add_or_not(name, grades): # считаем средний бал и решаем добавлять имя в список или нет
        value = 0
        for i in grades:
            value += i
        avarage_grade = value / 5

        if avarage_grade < 3.5:
            bad_grades_students_list.append(name)
            print(f"У студента {name} оценки {grades}, средний балл меньше 3.5: {avarage_grade}")

    add_or_not(name01, grades01) # делаем проверку для каждой пары имя-список оценок
    add_or_not(name02, grades02)
    add_or_not(name03, grades03)
    add_or_not(name04, grades04)
    add_or_not(name05, grades05)
    add_or_not(name06, grades06)

    return bad_grades_students_list

print(f"Отсортированный список студентов по имени: {sorted_students_names()}")
print()
print("Список студентов с низкой успеваемостью:")
print(bad_grades_students_list(
          Student01.get_name(), Student02.get_name(), Student03.get_name(),             # тоже очень топорно получается, но 6 объектов и у каждого по 2
          Student04.get_name(), Student05.get_name(), Student06.get_name(),             # атрибута с которыми нужно работать, так и получается 12 переменных
          Student01.get_progress(), Student02.get_progress(), Student03.get_progress(),
          Student04.get_progress(), Student05.get_progress(), Student06.get_progress(),
          ))

# Andrey = Student()
# Mark = Student()
# Anna = Student()
# Misha = Student()
# Sam = Student()
# Lia = Student()
# Wong = Student()
# Timur = Student()
# Dima = Student()
# Masha = Student()
# Eduard = Student()