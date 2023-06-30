# Задание № 1
#
# - Создайте класс Моя Строка, где:
#     - будут доступны все возможности str
#     - дополнительно хранятся имя автора строки и время создания (time.time)

from datetime import datetime as dt

__all__ = ['MyString']


class MyString(str):
    """Класс MyString, наследуемый от str и расширяющий её функционал, храня такие атрибуты,
    как имя автора и дату и время создания экземпляра класса"""

    def __new__(cls, value, author_name):
        """Конструктор класса MyString с двумя дополнительными атрибутами:
        имя автора (передаваемое в качестве аргумента) и дата и время создания строки"""
        obj = super().__new__(cls, value)
        obj._value = value
        obj._author_name = author_name
        obj._create_time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        return obj

    def get_author_name(self):
        """Метод, возвращающий имя автора"""
        return self._author_name

    def get_creation_time(self):
        """Метод, возвращающий дату и время создания строки"""
        return self._create_time

    def __str__(self):
        """Метод представления для пользователя"""
        return f"{self._create_time} {self._author_name} написал:\n{self._value}"

    def __repr__(self):
        """Метод представления для программиста"""
        return f"MyString('{self._value}', '{self._author_name}')"
