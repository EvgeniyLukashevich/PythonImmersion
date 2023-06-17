# SEMINAR 6. HOMEWORK. TASK 2
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


# SEMINAR 6. HOMEWORK. TASK 3
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел
# для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты
# и выведите 4 успешных расстановки.

from random import randint as ri

__all__ = ['peaceful_queens', 'peaceful_queens_check', 'print_field']
_queens = []


# Сгенерируем случайно стоящих ферзей
def several_queens(queens_count: int, field_x_size: int, field_y_size: int):
    global _queens
    _queens = []
    if queens_count > field_y_size * field_x_size:
        print("Ну слишком много ферзей или слишком уж маленькое поле :P")
        return False

    while len(_queens) < queens_count:
        queen = (ri(0, field_x_size - 1), ri(0, field_y_size - 1))

        # Это чтобы 2 ферзя не стояли на одной ячейке
        for q in _queens:
            if queen[0] == q[0] and queen[1] == q[1]:
                break
        else:
            _queens.append(queen)
    return True


# Метод, определяющий, является ли расстановка ферзей "небьющей"
def peaceful_queens_check(queens_count: int, field_x_size: int, field_y_size: int) -> bool:
    if not several_queens(queens_count, field_x_size, field_y_size):
        return False

    for i in range(len(_queens)):
        for j in range(i + 1, len(_queens)):
            # Проверяем, стоят ли i-тый и j-тый ферзи на одной вертикали, горизонтали или диагонали
            # С вертикалями и горизонталями - понятно.
            # С диагоналями:
            # если абсолютная разница координат по горизонтали равна абсолютной разнице координат по вертикали,
            # то наши ферзи стоят на одной диагонали
            if _queens[i][0] == _queens[j][0] \
                    or _queens[i][1] == _queens[j][1] \
                    or abs(_queens[i][0] - _queens[j][0]) == abs(_queens[i][1] - _queens[j][1]):
                return False
    return True


# Отрисовка поля с ферзями
def print_field(field_x_size, field_y_size):
    board = [['_' for x in range(field_x_size)] for y in range(field_y_size)]
    for queen in _queens:
        row, col = queen
        board[row][col] = 'Ф'

    print(' ', end='')
    for i in range(field_x_size):
        print(f' {i + 1}', end='')
    print('')

    for row in range(field_y_size):
        print(f'{row + 1}|', end='')
        for col in range(field_x_size):
            print(f'{board[row][col]}|', end='')
        print('')


# Метод, пытающийся вывести необходимое количество "небьющих" комбинаций ферзей за определенное количество итераций
def peaceful_queens(queens_count: int, field_x_size: int, field_y_size: int, iter_count: int, bingo_count: int):
    bingo = 0
    counter = 0

    while True:
        a = peaceful_queens_check(queens_count, field_x_size, field_y_size)

        if bingo == bingo_count:
            print(f"\nЗа {counter} итераций удалось сгенерировать {bingo_count} удачных расстановки")
            break
        if counter == iter_count:
            print(f"\nЗа {iter_count} итераций не удалось сгенерировать {bingo_count} удачных расстановки")
            break

        if a:
            bingo += 1
            counter += 1
            print(f"\nВариант удачной расстановки №{bingo}:")
            print_field(field_x_size, field_y_size)
        else:
            counter += 1
            continue


if __name__ == '__main__':
    peaceful_queens(8, 20, 20, 100000, 1)
