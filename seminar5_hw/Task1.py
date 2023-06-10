# SEMINAR 5. HOMEWORK. TASK 1
# Напишите функцию, которая принимает на вход строку -
# абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов:
# путь, имя файла, расширение файла.

import os


def filepath_split(filepath):
    """Метод, разделяющий путь до файла на три элемента (путь, имя файла, расширение файла).
    Args:
        filepath (str): Абсолютный путь до файла.
    Returns:
        Кортеж из трёх элементов: путь, имя файла, расширение файла.
    """
    filename, file_extension = os.path.splitext(filepath)
    path, filename = os.path.split(filename)
    return (path, filename, file_extension)


filepath = '/home/phive/projects/gb/python/readme.md'
print(filepath_split(filepath))
