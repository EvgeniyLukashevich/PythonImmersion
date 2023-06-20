# Задание № 6
#
# - Дорабатываем функции из предыдущих задач.
# - Генерируйте файлы в указанную директорию — отдельный параметр функции.
# - Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# - Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import string
from random import choices as rch
from random import randint as ri

__all__ = ['create_files3']


def _create_files_helper(
        directory, extension, min_name_length=6, max_name_length=30, min_size=256, max_size=4096, num_files=2
):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(num_files):
        file_name = ''.join(
            rch(string.ascii_letters + string.digits, k=ri(min_name_length, max_name_length))
        )
        file_path = os.path.join(directory, f"{file_name}.{extension}")

        if os.path.exists(file_path):
            continue

        file_size = ri(min_size, max_size)

        with open(file_path, 'wb') as f:
            f.write(os.urandom(file_size))

    print(f"Было создано {num_files} файлов с расширением {extension}.")


def create_files3(extensions_and_num_files: dict, directory, **kwargs):
    for extension, num_files in extensions_and_num_files.items():
        _create_files_helper(directory, extension, num_files=num_files, **kwargs)


