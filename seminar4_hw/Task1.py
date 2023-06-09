# SEMINAR 4. HOMEWORK. TASK 1
# Напишите функцию для транспонирования матрицы.
# (транспонирование матрицы - операция, при которой строки и столбцы матрицы меняются местами)

import random


def create_matrix(rows: int, cols: int) -> list:
    """
    Создает матрицу с заданным количеством строк и столбцов со случайными значениями от 1 до 10
    :param rows: количество строк
    :param cols: количество столбцов
    :return: новая матрица
    """
    matrix = []
    for i in range(rows):
        # Создаем список строки, заполненный случайными числами от 1 до 9
        row = [random.randint(1, 9) for j in range(cols)]
        matrix.append(row)

    return matrix


def print_matrix(matrix: list):
    for col in matrix:
        print(col)
    print()


def transpose_matrix(matrix: list) -> list:
    """
    Функция для транспонирования матрицы
    :param matrix: матрица, которую нужно транспонировать
    :return: транспонированная матрица
    """

    # Получаем количество строк и столбцов матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу для хранения транспонированной матрицы
    transposed_matrix = [[0 for j in range(rows)] for i in range(cols)]

    # Транспонируем матрицу, заполняя новую матрицу значениями из старой
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


matrix1 = create_matrix(3, 5)
print_matrix(matrix1)
matrix2 = transpose_matrix(matrix1)
print_matrix(matrix2)
