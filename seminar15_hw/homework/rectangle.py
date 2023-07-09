from .my_exceptions import RectangleSideTypeException, RectangleSideValueException
import logging
from datetime import datetime as dt

__all__ = ['Rectangle']

FORMAT = '{levelname} ; module_name:{name} ; line_number:{lineno} ; message:{msg}'
logging.basicConfig(
    filename='seminar15_hw/rectangle.log',filemode='a',encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


class Rectangle:
    """Класс Rectangle, хранящий длины сторон прямоугольника"""

    def __init__(self, side1: int | float, side2: int | float):
        if not isinstance(side1, int) and not isinstance(side1, float):
            logger.error(
                f"Введен некорректный тип данных для длины прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
            raise RectangleSideTypeException(side1)
        elif not isinstance(side2, int) and not isinstance(side2, float):
            logger.error(
                f"Введен некорректный тип данных для ширины прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
            raise RectangleSideTypeException(side2)
        elif side1 <= 0:
            logger.error(
                f"Введено отрицательное значение для длины прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
            raise RectangleSideValueException(side1)
        elif side2 <= 0:
            logger.error(
                f"Введено отрицательное значение для ширины прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
            raise RectangleSideValueException(side2)
        else:
            self._side1 = side1
            self._side2 = side2
            logger.info(
                f"Прямоугольник успешно создан ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")


    @property
    def perimeter(self):
        """Метод возвращающий периметр прямоугольника"""
        logger.info(
            f"Вычислен периметр прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return self._side1 * 2 + self._side2 * 2

    @property
    def area(self):
        """Метод возвращающий площадь прямоугольника"""
        logger.info(
            f"Вычислена площадь прямоугольника ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return self._side1 * self._side2

    def __str__(self):
        """Метод представления для пользователя"""
        logger.info(
            f"Свойства прямоугольника выведены в консоль ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return f"Сторона a: {self._side1}\n" \
               f"Сторона b: {self._side2}\n" \
               f" Периметр: {self.perimeter}\n" \
               f"  Площадь: {self.area}\n"

    def __repr__(self):
        logger.info(
            f"Представление для программиста выведено консоль ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return f'Rectangle({self._side1}, {self._side2})'

    def __add__(self, other):
        """Метод реализующий логику сложения экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.perimeter + other.perimeter
            side1 = perimeter / 4 + perimeter / 8
            side2 = perimeter / 4 - perimeter / 8
            logger.info(
                f"Выполнено сложение прямоугольников ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
            return Rectangle(side1, side2)
        else:
            logger.error(
                f"Объект не является экземпляром класса Rectangle ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def __sub__(self, other):
        """Метод реализующий логику вычитания экземпляров класса Rectangle"""
        if isinstance(other, Rectangle):
            perimeter = self.perimeter - other.perimeter
            if perimeter > 0:
                side1 = perimeter / 4 + perimeter / 8
                side2 = perimeter / 4 - perimeter / 8
                logger.info(
                    f"Выполнено вычитание прямоугольников ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
                return Rectangle(side1, side2)
            else:
                logger.error(
                    f"В результате вычитания получен отрицательный периметр ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            logger.error(
                f"Объект не является экземпляром класса Rectangle ; {dt.now().strftime('%Y-%m-%d %H:%M:%S')}")
