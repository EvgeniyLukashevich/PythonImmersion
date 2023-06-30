__all__ = ['Matrix']


class Matrix:
    def __init__(self, matrix):
        """Инициализатор класса Matrix, принимающий в качестве аргумента список списков"""
        self._matrix = matrix

    def __str__(self):
        """Метод представления для пользователя"""
        return '\n'.join(['  '.join([str(cell) for cell in row]) for row in self._matrix])

    def __repr__(self):
        """Метод представления для программиста"""
        return f"Matrix({self._matrix})"

    def __eq__(self, other):
        """Метод сравнения матриц на предмет их равенство (истина, если размеры матриц совпадают)"""
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) == len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) < len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) > len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) <= len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) >= len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __add__(self, other):
        """Метод сложения матриц"""
        if isinstance(other, Matrix):
            if self.__eq__(other):
                matrix = []
                for i in range(len(self._matrix)):
                    row = []
                    for j in range(len(self._matrix[i])):
                        element = self._matrix[i][j] + other._matrix[i][j]
                        row.append(element)
                    matrix.append(row)
                return Matrix(matrix)
            else:
                print("Размеры матриц не совпадают")
        else:
            print("Объект не является экземпляром класса Matrix")

    def __mul__(self, other):
        """Метод умножения матриц"""
        if isinstance(other, Matrix):
            if self.__eq__(other):
                matrix = []
                for i in range(len(self._matrix)):
                    row = []
                    for j in range(len(self._matrix[i])):
                        element = self._matrix[i][j] * other._matrix[i][j]
                        row.append(element)
                    matrix.append(row)
                return Matrix(matrix)
            else:
                print("Размеры матриц не совпадают")
        else:
            print("Объект не является экземпляром класса Matrix")
