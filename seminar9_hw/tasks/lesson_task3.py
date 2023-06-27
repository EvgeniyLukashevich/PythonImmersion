# ## Задание № 3
#
# - Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
#   и результат, который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# - Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# - Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# - Имя файла должно совпадать с именем декорируемой функции.


import json
from typing import Callable


def params_to_json(func: Callable):
    filename = f"{func.__name__}.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except:
        data = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filename = f"{func.__name__}.json"
        with open(filename, 'w') as file:
            dict = {'args': args}

            for key in kwargs:
                dict[key] = kwargs[key]

            data.append({result: dict})
            json.dump(data, file, indent=2)
            print(f"Данные в файл '{filename}' успешно записаны")

        return result

    return wrapper


@params_to_json
def my_sum(*args: int | float, **kwargs: int | float) -> int:
    result = sum(args)

    for key in kwargs:
        result += kwargs[key]

    return result


if __name__ == '__main__':
    print(my_sum(1, 2, 3, num4=4, num5=5))
    print(my_sum(1))
    print(my_sum(3, 7))
    print(my_sum(num1=12, num2=15))
