# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint as ri
from sys import argv


# Пропишем в функции значения "по умолчанию" для аргументов.
def guess_number_console(tries_count: int = 10, lower_limit: int = 0, upper_limit: int = 100) -> bool:
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
    # Распаковываем в аргументы функции параметры введенные из терминала, за исключением первого (путь к файлу)
    print(guess_number_console(*(int(num) for num in argv[1:])))
