from typing import Callable
from random import randint as ri


__all__=['guessing_game']

def values_control(func: Callable):
    NUMBER_MIN = 1
    NUMBER_MAX = 100
    TRIES_MIN = 1
    TRIES_MAX = 10

    def wrapper(*args):
        number, tries = args

        if not NUMBER_MIN <= number <= NUMBER_MAX:
            print("Некорректное число.\nЗамена аргумента на рандомное число от 1 до 100\n")
            number = ri(1, 100)

        if not TRIES_MIN <= tries <= TRIES_MAX:
            print("Некорректное количество попыток.\nЗамена аргумента на рандомное число от 1 до 10\n")
            tries = ri(1, 10)

        return func(number, tries)

    return wrapper


@values_control
def guessing_game(secret_number: int, max_tries: int):
    counter = 0

    while counter < max_tries:
        counter += 1
        guess = int(input(f'Попытка {counter} из {max_tries}:\nУгадайте число от 1 до 100: '))

        if guess == secret_number:
            print(f'\nПоздравляем! Вы угадали!\nЧисло: {secret_number}. Количество попыток: {counter}')
            break
        elif guess < secret_number:
            print('Загаданное число больше\n')
        else:
            print('Загаданное число меньше\n')
    else:
        print(f'Игра окончена! Было загадано число {secret_number}')


if __name__ == '__main__':
    guessing_game(500, 15)



