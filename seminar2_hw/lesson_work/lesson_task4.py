# TASK 4. Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math

# получаем диаметр от пользователя
diameter = float(input("Введите диаметр круга: "))

# вычисляем площадь круга
radius = diameter / 2
area = math.pi * radius ** 2
print(f"Площадь круга: {area:.42f}")

# вычисляем длину окружности
circumference = math.pi * diameter
print(f"Длина окружности: {circumference:.42f}")
