print('GB Lesson 8')

# 1, 2, 3
# "abc"
# [10, 20, 30]

# print(type(1))
# print(type("abc"))
# print(type([10, 20, 30]))

# class Fruit:
#     pass
#
# a = Fruit()
# b = Fruit()
#
# a.name = "apple"
# a.weight = 120
#
# b.name = "orange"
# b.weight = 150
#
# print(a.name, a.weight)
# print(b.name, b.weight)
#
# b.weight -= 50
#
# print(a.name, a.weight)
# print(b.name, b.weight)
# class Hello:
#     def hello_world(self):
#         print("Привет, Мир!")
#
#     def greeting(self, name):
#         print(f"Привет, {name}")
#
# greet = Hello()
# greet.hello_world()
# greet.greeting("Bob")


# class Car:
#
#     def __init__(self, color):
#         self.e_on = False
#         self.color = color
#
#     def start(self):
#         self.e_on = True
#
#     def drive_to(self, city):
#         if self.e_on:
#             print(f"Едем в {city} на {self.color} авто")
#         else:
#             print("Никуда не едему - заведите авто")
#
# c = Car("красный")
# c.start()
# c.drive_to('Сочи')
# print(1 + 2)
# print(1.3 + 2.5)
# print('1.3' + '2.5')
#
# def f(x, y):
#     return x + y
#
# print(f(1, 2))
# print(f('1.3', '2.5'))


# class Book:
#     def __init__(self, name,  auth):
#         self.name = name
#         self.auth = auth
#
#     def get_name(self):
#         return self.name
#
#     def get_auth(self):
#         return self.auth
#
# book = Book('Война и мир', 'Толстой')
#
# print(f"книга - {book.get_name()}, автор - {book.get_auth()}")
om math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#     def perimeter(self):
#         return  2 * pi * self.radius
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
#
#
# def print_shape_info(shape):
#     print(f'Area = {shape.area()}, perimeter = {shape.perimeter()}')
#
# square = Square(10)
# # print(square.area())
# # print(square.perimeter())
# print_shape_info(square)
#
# circle = Circle(10)
# print_shape_info(circle)
