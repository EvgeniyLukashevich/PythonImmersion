#  Задание № 1
#
# - Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов
# - Возвращается строка в нижнем регистре.

#  Задание № 2
#
# - Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
#     - возврат строки без изменений
#     - возврат строки с преобразованием регистра без потери символов
#     - возврат строки с удалением знаков пунктуации
#     - возврат строки с удалением букв других алфавитов
#     - возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import doctest

__all__ = ['clean_text']

__AllOWED_CHARS = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')


def clean_text(text):
    """
    Функция, получающая на вход строку и удаляющая все символы, кроме символов латинского алфавита и пробелов.
    Возвращает строку в нижнем регистре.
    >>> clean_text('hello world')
    'hello world'
    >>> clean_text("Hello WORLD")
    'hello world'
    >>> clean_text("hello, world")
    'hello world'
    >>> clean_text("hello мир")
    'hello '
    >>> clean_text("Hello, мир! Привет, world!")
    'hello   world'
    """
    cleaned_text = ''.join(c for c in text if c in __AllOWED_CHARS)
    return cleaned_text.lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
