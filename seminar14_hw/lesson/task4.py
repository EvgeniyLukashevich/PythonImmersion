#  Задание № 4
#
# - Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
#     - возврат строки без изменений
#     - возврат строки с преобразованием регистра без потери символов
#     - возврат строки с удалением знаков пунктуации
#     - возврат строки с удалением букв других алфавитов
#     - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest
from .task1_2 import clean_text


def test1():
    assert clean_text('hello world') == 'hello world', 'Должна была вернуться строка без изменений'


def test2():
    assert clean_text('Hello WORLD') == 'hello world', \
        'Должна была вернуться строка с преобразованием регистра без потери символов'


def test3():
    assert clean_text('hello, world') == 'hello world', 'Должна была вернуться строка с удалением знаков пунктуации'


def test4():
    assert clean_text('hello мир') == 'hello ', 'Должна была вернуться строка с удалением букв других алфавитов'


def test_final():
    assert clean_text('Hello, мир! Привет, world!') == 'hello   world', \
        'Должна была вернуться строка с учётом всех вышеперечисленных пунктов'


if __name__ == '__main__':
    pytest.main()
