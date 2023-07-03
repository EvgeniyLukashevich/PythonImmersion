from .my_exceptions import RectangleSideTypeException, RectangleSideValueException

__all__ = ['Rectangle']


class Rectangle:
    """Класс Rectangle, хранящий длины сторон прямоугольника"""

    def __init__(self, side1: int, side2: int):
        if not isinstance(side1, int):
            raise RectangleSideTypeException(side1)
        elif not isinstance(side2, int):
            raise RectangleSideTypeException(side2)
        elif side1 <= 0:
            raise RectangleSideValueException(side1)
        elif side2 <= 0:
            raise RectangleSideValueException(side2)
        else:
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
