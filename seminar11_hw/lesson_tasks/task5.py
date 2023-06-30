# Задание № 5
#
# - Дорабатываем класс прямоугольник из прошлого семинара.
# - Добавьте возможность сложения и вычитания.
# - При этом должен создаваться новый экземпляр прямоугольника.
# - Складываем и вычитаем периметры, а не длину и ширину.
# - При вычитании не допускайте отрицательных значений.

__all__ = ['Rectangle']


class Rectangle:
    """Класс Rectangle, хранящий длины сторон прямоугольника"""

    def __init__(self, side1: int | float, side2: int | float):
        self._side1 = side1
        self._side2 = side2

    def get_perimeter(self):
        """Метод возвращающий периметр прямоугольника"""
        return self._side1 * 2 + self._side2 * 2

    def get_area(self):
        """Метод возвращающий площадь прямоугольника"""
        return self._side1 * self._side2

    def __str__(self):
        """Метод представления для пользователя"""
        return f"Сторона a: {self._side1}\n" \
               f"Сторона b: {self._side2}\n" \
               f" Периметр: {self.get_perimeter()}\n" \
               f"  Площадь: {self.get_area()}\n"

    def __repr__(self):
        return f'Rectangle({self._side1}, {self._side2})'

    def __add__(self, other):
        """Метод реализующий логику сложения экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.get_perimeter() + other.get_perimeter()
            side1 = perimeter / 4 + perimeter / 8
            side2 = perimeter / 4 - perimeter / 8
            return Rectangle(side1, side2)
        else:
            print(f"Объект не является экземпляром класса Rectangle")

    def __sub__(self, other):
        """Метод реализующий логику вычитания экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.get_perimeter() - other.get_perimeter()
            if perimeter > 0:
                side1 = perimeter / 4 + perimeter / 8
                side2 = perimeter / 4 - perimeter / 8
                return Rectangle(side1, side2)
            else:
                print(f"В результате вычитания получен отрицательный периметр")
        else:
            print(f"Объект не является экземпляром класса Rectangle")
