# Задание № 4
#
# - Создайте декоратор с параметром.
# - Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable
from random import randint as ri


def reusable_start(iterations_count: int = 5):
    def deco(func: Callable):
        new_list = []

        def wrapper(*args, **kwargs):
            print("\n# # # # # # # # # # # # # # # # # # # # # # # #")
            for i in range(iterations_count):
                print(f"\nИтерация {i + 1}")
                result = func(*args, **kwargs)
                new_list.append(result)
            return new_list

        return wrapper

    return deco


@reusable_start(3)
def random_sum(number_min: int = 1, number_max: int = 10) -> int:
    num1 = ri(number_min, number_max)
    num2 = ri(number_min, number_max)
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result


if __name__ == '__main__':
    print(f'\nСписок результатов: {random_sum(15, 25)}')
    print(f'\nСписок результатов: {random_sum()}')
    print(f'\nСписок результатов: {random_sum(number_min=50, number_max=100)}')



