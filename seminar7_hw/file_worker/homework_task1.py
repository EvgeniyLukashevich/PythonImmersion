# ### HOMEWORK. Task 1
#
# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени.
# Например, для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.

import os

__all__ = ['rename_files']


def rename_files(
        dir: str, final_name: str,
        num_digits: int, source_extension: str,
        dest_extension: str, char_range: list):

    counter = 0
    for filename in os.listdir(dir):
        if filename.endswith(source_extension):
            name = filename[char_range[0]:char_range[1]]
            if final_name is not None:
                name += final_name
                name += str(counter).zfill(num_digits) + dest_extension
                os.rename(os.path.join(dir, filename), os.path.join(dir, name))
                counter += 1

