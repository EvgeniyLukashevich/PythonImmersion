from .rectangle_side_exception import RectangleSideException


class RectangleSideValueException(RectangleSideException):
    def __init__(self, side):
        super().__init__(side)

    def __str__(self):
        return super().__str__() + f"Длина стороны должна быть больше нуля\n"
