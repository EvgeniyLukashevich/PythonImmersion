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
        """
        Метод сравнения матриц на предмет их равенства (истина, если размеры матриц совпадают)
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) == Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        >>> Matrix([[1, 2], [3, 4]]) == Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        """
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) == len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __ne__(self, other):
        """
        Метод сравнения матриц на предмет их неравенства (истина, если размеры матриц не совпадают)
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) != Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        >>> Matrix([[1, 2], [3, 4]]) != Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Метод сравнения матриц на предмет того, что левая строго меньше правой
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) < Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        >>> Matrix([[1, 2], [3, 4]]) < Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) < Matrix([[2, 3], [1, 2], [1, 2]])
        False
        """
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) < len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __gt__(self, other):
        """
        Метод сравнения матриц на предмет того, что левая строго больше правой
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) > Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        >>> Matrix([[1, 2], [3, 4]]) > Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) > Matrix([[2, 3], [1, 2], [1, 2]])
        True
        """
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) > len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __le__(self, other):
        """
        Метод сравнения матриц на предмет того, что левая меньше либо равна правой
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) <= Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        >>> Matrix([[1, 2], [3, 4]]) <= Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) <= Matrix([[2, 3], [1, 2], [1, 2]])
        False
        """
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) <= len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __ge__(self, other):
        """
        Метод сравнения матриц на предмет того, что левая больше либо равна правой
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) >= Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        True
        >>> Matrix([[1, 2], [3, 4]]) >= Matrix([[2, 3, 1], [1, 2, 4], [1, 2, 1]])
        False
        >>> Matrix([[1, 2, 2], [3, 4, 1], [3, 1, 3]]) >= Matrix([[2, 3], [1, 2], [1, 2]])
        True
        """
        if isinstance(other, Matrix):
            return len(self._matrix) * len(self._matrix[0]) >= len(other._matrix) * len(other._matrix[0])
        else:
            return False

    def __add__(self, other):
        """
        Метод сложения матриц
        >>> isinstance(Matrix([[2, 2], [2, 2]]) + Matrix([[3, 3], [3, 3]]), Matrix)
        True
        >>> Matrix([[2, 2], [2, 2]]) + Matrix([[3, 3, 3], [3, 3, 3]])
        Размеры матриц не совпадают
        >>> Matrix([[2, 2], [2, 2]]) + [[3, 3, 3], [3, 3, 3]]
        Объект не является экземпляром класса Matrix
        """
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
        """
        Метод умножения матриц
        >>> isinstance(Matrix([[2, 2], [2, 2]]) * Matrix([[3, 3], [3, 3]]), Matrix)
        True
        >>> Matrix([[2, 2], [2, 2]]) * Matrix([[3, 3, 3], [3, 3, 3]])
        Размеры матриц не совпадают
        >>> Matrix([[2, 2], [2, 2]]) * [[3, 3, 3], [3, 3, 3]]
        Объект не является экземпляром класса Matrix
        """
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
