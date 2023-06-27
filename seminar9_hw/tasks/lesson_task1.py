# ## Задание № 1
#
# - Создайте функцию-замыкание, которая запрашивает два целых числа:
#     - от 1 до 100 для загадывания.
#     - от 1 до 10 для количества попыток.
# - Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.

from random import randint as ri


def guessing_game(max_tries: int = 10):
    secret_number = ri(1, 100)

    def playing():
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

    return playing


if __name__ == '__main__':
    guessing_game(7)()
