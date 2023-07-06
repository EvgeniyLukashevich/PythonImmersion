#  Задание № 5
#
# - На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
#   а также вычисляющую периметр, площадь
#   и позволяющий складывать и вычитать прямоугольники беря за основу периметр
# - Напишите 3-7 тестов unittest для данного класса

from seminar13_hw.homework.rectangle import Rectangle
import unittest


class RectangleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(2, 3)
        self.r2 = Rectangle(4, 5)

    def test_area(self):
        self.assertEqual(self.r1.area, 6, "Неверно вычисляется площадь прямоугольника")

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter, 10, "Неверно вычисляется периметр прямоугольника")

    def test_sum_result_type(self):
        self.assertIsInstance(self.r1 + self.r2, Rectangle,
                              "В результате сложения прямоугольников получился не прямоугольник")

    def test_sum(self):
        self.assertEqual((self.r1 + self.r2).perimeter, self.r1.perimeter + self.r2.perimeter,
                         "Сложение прямоугольников происходит не путём сложения периметров")


if __name__ == '__main__':
    unittest.main(verbosity=2)
