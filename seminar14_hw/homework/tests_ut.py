import unittest
from seminar14_hw.homework.matrix import Matrix


class MatrixTest(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix1 = Matrix([[2, 2], [2, 2]])
        self.matrix2 = Matrix([[3, 3], [3, 3]])
        self.matrix3 = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])

    def test_equal(self):
        self.assertEqual(self.matrix1, self.matrix2,
                         msg='Сравнение на равенство (размерности матриц) работает некорректно')

    def test_not_equal(self):
        self.assertNotEqual(self.matrix1, self.matrix3,
                            msg='Сравнение на неравенство (размерности матриц) работает некорректно')

    def test_greater(self):
        self.assertGreater(
            self.matrix3,
            self.matrix1,
            msg='Сравнение на то, что левая матрица (размерность матрицы) больше правой работает некорректно')

    def test_sum_result_type(self):
        self.assertIsInstance(self.matrix1 + self.matrix2, Matrix,
                              msg='Сложения матриц возвращает результат некорректного типа')

    def test_mult_result_type(self):
        self.assertIsInstance(self.matrix1 * self.matrix2, Matrix,
                              msg='Умножение матриц возвращает результат некорректного типа')


if __name__ == '__main__':
    unittest.main(verbosity=2)
