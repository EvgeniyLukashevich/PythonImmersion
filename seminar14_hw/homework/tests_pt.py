import pytest
from seminar14_hw.homework.matrix import Matrix

matrix1 = Matrix([[2, 2], [2, 2]])
matrix2 = Matrix([[3, 3], [3, 3]])
matrix3 = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])


def test_equal():
    assert matrix1 == matrix2, 'Сравнение на равенство (размерности матриц) работает некорректно'


def test_not_equal():
    assert matrix1 != matrix3, 'Сравнение на неравенство (размерности матриц) работает некорректно'


def test_greater():
    assert matrix3 > matrix1, \
        'Сравнение на то, что левая матрица (размерность матрицы) больше правой работает некорректно'


def test_sum_result_type():
    assert isinstance(matrix1 + matrix2, Matrix), 'Сложения матриц возвращает результат некорректного типа'


def test_multiply_result_type():
    assert isinstance(matrix1 * matrix2, Matrix), 'Сложения матриц возвращает результат некорректного типа'


if __name__ == '__main__':
    pytest.main()
