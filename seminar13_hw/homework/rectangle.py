from seminar13_hw.homework.my_exceptions import RectangleSideTypeException, RectangleSideValueException

__all__ = ['Rectangle']


class Rectangle:
    """Класс Rectangle, хранящий длины сторон прямоугольника"""

    def __init__(self, side1: int | float, side2: int | float):
        if not isinstance(side1, int) and not isinstance(side1, float):
            raise RectangleSideTypeException(side1)
        elif not isinstance(side2, int) and not isinstance(side2, float):
            raise RectangleSideTypeException(side2)
        elif side1 <= 0:
            raise RectangleSideValueException(side1)
        elif side2 <= 0:
            raise RectangleSideValueException(side2)
        else:
            self._side1 = side1
            self._side2 = side2

    @property
    def perimeter(self):
        """Метод возвращающий периметр прямоугольника"""
        return self._side1 * 2 + self._side2 * 2

    @property
    def area(self):
        """Метод возвращающий площадь прямоугольника"""
        return self._side1 * self._side2

    def __str__(self):
        """Метод представления для пользователя"""
        return f"Сторона a: {self._side1}\n" \
               f"Сторона b: {self._side2}\n" \
               f" Периметр: {self.perimeter}\n" \
               f"  Площадь: {self.area}\n"

    def __repr__(self):
        return f'Rectangle({self._side1}, {self._side2})'

    def __add__(self, other):
        """Метод реализующий логику сложения экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.perimeter + other.perimeter
            side1 = perimeter / 4 + perimeter / 8
            side2 = perimeter / 4 - perimeter / 8
            return Rectangle(side1, side2)
        else:
            print(f"Объект не является экземпляром класса Rectangle")

    def __sub__(self, other):
        """Метод реализующий логику вычитания экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.perimeter - other.perimeter
            if perimeter > 0:
                side1 = perimeter / 4 + perimeter / 8
                side2 = perimeter / 4 - perimeter / 8
                return Rectangle(side1, side2)
            else:
                print(f"В результате вычитания получен отрицательный периметр")
        else:
            print(f"Объект не является экземпляром класса Rectangle")


if __name__ == '__main__':
    r = Rectangle('two', 2)
    print(r)
