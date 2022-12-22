
# print(type(1))
# print(type("abc"))
# print(type([1, 2, 3]))

# class Fruit: # классы с большой буквы смю PIP8
#     pass
#
# a = Fruit() # экземпляры класса
# b = Fruit()
#
# a.name = "apple" # атрибуты(свойства) экземпляра
# a.weight = 120
#
# b.name = "orange" # атрибуты(свойства) экземпляра
# b.weight = 150
#
# b.weight -= 50
#
# print(a.name, a.weight)
# print(b.name, b.weight)
#
# class Hello:
#     def hello_world(self): # функция/метод, должен быть обязательно аргумент, в данном случае self назыать так, показывает что относятся к самой себе
#                            # и как я понял нужен чтобы работать на объекте. Без него будет работать без объекта, как статический класс в C#.
#         print("Привет, Мир!")
#
#     def greeting(self, name):
#         print(f"Привет, {name}!")
#     def greeting_without(name): # без self получается что мы работаем без объекта, как статический класс в C#, потому вызывать нужно по другому
#         print(f"Привет, {name}!")
#
#
#
# greet = Hello() # экземпляр класса Hello
# greet.hello_world()
# # greet.greeting("Misha")
#
# Hello.hello_world(greet) # так работает за счёт self
# greet.greeting("Misha") # так работает за счёт self
# Hello.greeting_without("Sam") # пример работы без объекта/экземпляра

#
# class Car:
#     def __init__(self, color):
#         self.e_on = False # свойство класса со значением по умолчанию
#         self.color = color # свойство класса, которое мы должны задать при создании экземпляра
#
#     def start(self):
#         self.e_on = True # self добавляется чтобы разные методы внутри одного класса могли использовать одну переменную(свойство), как я понял
#
#     def drive_to(self, city):
#         if self.e_on:
#             print(f"Едем в {city} на {self.color} авто") # self.color пишем так как определена в другом методе
#         else:
#             print("Никуда не едем - заведите авто")
#
# c = Car("белый")
# c.start() # если этот метод не выполнить, то программа выведет "Никуда не едем"
# c.drive_to("Сочи")

# print(1+2)
# print(1.34+2.24)
# print("1.34"+"2.24")

# class Book:
#     def __init__(self, name, auth):
#         self.name = name
#         self.auth = auth
#
#     def get_name(self):
#         return self.name
#
#     def get_auth(self):
#         return self.auth
#
# book = Book("Война и мир", "Толстой")
# print(f"книга - {book.get_name()}, автор - {book.get_auth()}") # через методы - безопаснее, так как значение нельзя изменить
# print(f"книга - {book.name}, автор - {book.auth}") # через свойства класса


# # полиморфизм:
# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def perimeter(self):
#         return 2 * pi * self.radius
#
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
#     def perimeter(self):
#         return 4 * self.side
#
# def print_shape_info(shape): # на вход можно подать объекты разных классов, но отрабатывать будет корректно
#     print(f'Area = {shape.area()}, perimeter = {shape.perimeter()}')
#
# square = Square(10)
# print(square.area())
# print(square.perimeter())
#
# print_shape_info(square)
#
# square = Circle(10)
# print_shape_info(square)









