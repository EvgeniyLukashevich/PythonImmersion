# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as ri

__all__ = ['guess_number']


def guess_number(lower_limit: int, upper_limit: int, tries_count: int) -> bool:
    bingo = ri(lower_limit, upper_limit)

    while tries_count > 0:
        print(f"Осталось попыток: {tries_count}")
        user_number = int(input(f"Угадай число от {lower_limit} до {upper_limit} (включительно):"))

        if bingo == user_number:
            print(f"Число {bingo} угадано")
            return True

        elif bingo < user_number:
            print(f"Загаданное число меньше, чем {user_number}")

        else:
            print(f"Загаданное число больше, чем {user_number}")

        tries_count -= 1

    print(f"Было загадано число {bingo}. Попытки исчерпаны. Ты не угадал :(")
    return False


if __name__ == '__main__':
    print(guess_number(0, 100, 10))
