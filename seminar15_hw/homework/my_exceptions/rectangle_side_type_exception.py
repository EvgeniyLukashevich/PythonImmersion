from .rectangle_side_exception import RectangleSideException


class RectangleSideTypeException(RectangleSideException):
    def __init__(self, side):
        super().__init__(side)

    def __str__(self):
        return super().__str__() + f"Необходимо ввести данные типа int или float\n"
