

class RectangleSideException(Exception):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"\nНекорректные данные для одной из сторон прямоугольника: {self.side}\n"
