#  Задание № 3
#
# - Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
#     - возврат строки без изменений
#     - возврат строки с преобразованием регистра без потери символов
#     - возврат строки с удалением знаков пунктуации
#     - возврат строки с удалением букв других алфавитов
#     - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest
from .task1_2 import clean_text


class CleanTextTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            clean_text('hello world'),
            'hello world',
            msg='Должна была вернуться строка без изменений')

    def test2(self):
        self.assertEqual(
            clean_text('Hello WORLD'),
            'hello world',
            msg='Должна была вернуться строка с преобразованием регистра без потери символов')

    def test3(self):
        self.assertEqual(
            clean_text('hello, world'),
            'hello world',
            msg='Должна была вернуться строка с удалением знаков пунктуации')

    def test4(self):
        self.assertEqual(
            clean_text('hello мир'),
            'hello ',
            msg='Должна была вернуться строка с удалением букв других алфавитов')

    def test_final(self):
        self.assertEqual(
            clean_text('Hello, мир! Привет, world!'),
            'hello   world',
            msg='Должна была вернуться строка с учётом всех вышеперечисленных пунктов')


if __name__ == '__main__':
    unittest.main(verbosity=2)


