#  Задание № 4
#
# - Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
#     - расширение
#     - минимальная длина случайно сгенерированного имени, по умолчанию 6
#     - максимальная длина случайно сгенерированного имени, по умолчанию 30
#     - минимальное число случайных байт, записанных в файл, по умолчанию 256
#     - максимальное число случайных байт, записанных в файл, по умолчанию 4096
#     - количество файлов, по умолчанию 42
# - Имя файла и его размер должны быть в рамках переданного диапазона.

import os
from random import choices as rch
from random import randint as ri
import string

__all__ = ['create_files']


def create_files(extension, min_name_length=6, max_name_length=30, min_size=256, max_size=4096, num_files=2):
    for i in range(num_files):
        file_name = ''.join(
            rch(string.ascii_letters + string.digits, k=ri(min_name_length, max_name_length))
        )
        file_path = f"{file_name}.{extension}"

        file_size = ri(min_size, max_size)

        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))

    print(f"Было создано {num_files} файлов с расширением {extension}.")



