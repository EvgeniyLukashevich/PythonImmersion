from lesson_tasks import *
from homework_task2 import *

# Домашнее задание
matrix1 = Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]])
print(f"\nМатрица 1:\n{matrix1}")
matrix2 = Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
print(f"\nМатрица 2:\n{matrix2}")
matrix_another_length = Matrix(([[1, 1, 1], [2, 2, 2]]))
print(f"\nМатрица другого размера:\n{matrix_another_length}")

matrix3 = matrix1 + matrix2
print(f"\nМатрица 1 + Матрица 2:\n{matrix3}")

matrix3 = matrix1 * matrix2
print(f"\nМатрица 1 * Матрица 2:\n{matrix3}")

print(f"\nМатрица 1 + Матрица другого размера:")
matrix3 = matrix1 + matrix_another_length

print(f"\nМатрица 1 == Матрица 2: {matrix1 == matrix2}")
print(f"\nМатрица 1 != Матрица другого размера: {matrix1 != matrix_another_length}")
print(f"\nМатрица 1 < Матрица другого размера: {matrix1 < matrix_another_length}")
print(f"\nМатрица 2 >= Матрица другого размера: {matrix2 >= matrix_another_length}")

print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")

# # Задание № 1 с семинара
# welcome_line = MyString('Добро пожаловать!', 'Евгений')
# print(welcome_line)
#
# print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")
#
# # Задание № 2 с семинара
# values1 = Archive(1, "Один")
# print(f"Архив чисел: {values1.get_numbers()}\nАрхив строк: {values1.get_strings()}\n")
# values2 = Archive(2, "Два")
# print(f"Архив чисел: {values1.get_numbers()}\nАрхив строк: {values1.get_strings()}\n")
# values3 = Archive(3, "Три")
# print(f"Архив чисел: {values1.get_numbers()}\nАрхив строк: {values1.get_strings()}\n")
#
# print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")
#
# # Задание № 4 с семинара
# print(values1)
# print(f"{values1 = }")
#
# print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")
#
# # Задание № 5 с семинара
# rectangle1 = Rectangle(8, 4)
# print(f"Прямоугольник 1:\n{rectangle1}")
#
# rectangle2 = Rectangle(10, 8)
# print(f"Прямоугольник 2:\n{rectangle2}")
#
# not_rectangle = [2, 5]
#
# rectangle3 = rectangle1 + rectangle2
# print(f"Прямоугольник 1 + Прямоугольник 2:\n{rectangle3}")
#
# rectangle3 = rectangle2 - rectangle1
# print(f"Прямоугольник 2 - Прямоугольник 1:\n{rectangle3}")
#
# print(f"Прямоугольник 1 - Прямоугольник 2:")
# rectangle3 = rectangle1 - rectangle2
#
# print(f"\nПрямоугольник 1 + Не прямоугольник:")
# rectangle3 = rectangle1 + not_rectangle
#
# print("\n# # # # # # # # # # # # # # # # # # # # # # # #\n")
