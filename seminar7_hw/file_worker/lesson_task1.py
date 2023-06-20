# Задание № 1
#
# - Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# - Первое число int, второе - float разделены вертикальной чертой.
#       Минимальное число - -1000, максимальное - +1000.
# - Количество строк и имя файла передаются как аргументы функции.

from random import randint as ri
from random import uniform as ru
from pathlib import Path

__all__ = ['int_float_writer']

_MIN_NUMBER = -1000
_MAX_NUMBER = 1000


def int_float_writer(file_name: str | Path, lines_count: int):
    with open(file_name, 'a', encoding='utf-8') as file:
        # Непонятно, нужно ли генерировать новую пару чисел для каждой строки
        # Или записывать одну и ту же пару на каждую строку
        for _ in range(lines_count):
            print(f'{ri(_MIN_NUMBER, _MAX_NUMBER)}|{ru(_MIN_NUMBER, _MAX_NUMBER)}', file=file)


