# Задание № 5
#
# - Объедините функции из прошлых задач.
# - Функцию угадайку задекорируйте:
#     - декораторами для сохранения параметров
#     - декоратором контроля значений
#     - декоратором для многократного запуска
# - Выберите верный порядок декораторов

from lesson_task2 import values_control
from lesson_task3 import params_to_json
from lesson_task4 import reusable_start


@reusable_start(2)
@values_control
@params_to_json
def guessing_game(secret_number: int, max_tries: int):
    counter = 0

    while counter < max_tries:
        counter += 1
        guess = int(input(f'Попытка {counter} из {max_tries}:\nУгадайте число от 1 до 100: '))

        if guess == secret_number:
            print(f'\nПоздравляем! Вы угадали!\nЧисло: {secret_number}. Количество попыток: {counter}')
            return True
        elif guess < secret_number:
            print('Загаданное число больше\n')
        else:
            print('Загаданное число меньше\n')
    else:
        print(f'Игра окончена! Было загадано число {secret_number}')
        return False


if __name__ == '__main__':
    guessing_game(300, 25)
