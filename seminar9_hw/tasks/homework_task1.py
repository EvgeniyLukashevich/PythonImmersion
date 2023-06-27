# Seminar 9. Homework. Task 1.
#
# - Напишите следующие функции:
#     - Нахождение корней квадратного уравнения
#     - Генерация csv файла с тремя случайными числами в каждой строке (100-1000 строк)
#     - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
#     - Декоратор, сохраняющий переданные параметры и результаты работы функции в json-файл


from typing import Callable
import math
import csv
import json
from functools import wraps
import random

__all__ = ['quadratic_equation', 'generate_csv']


def generate_csv(filename: str, lines_count: int):
    """Функция для генерации csv файла с заданным количеством строк,
    каждая строка содержит 3 случайных числа"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(lines_count):
            row = [random.randint(-100, 100) for j in range(3)]
            writer.writerow(row)


def quadratic_equation_from_csv(filename: str):
    def deco(func: Callable):
        """Декоратор для нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла"""

        def wrapper(*args):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    a, b, c = row
                    result = func(int(a), int(b), int(c))
                    print(f"Уравнение: ({a})*x^2 + ({b})*x + ({c}) = 0\nКорни: {result}\n")

        return wrapper

    return deco


def save_to_json(filename: str):
    """Декоратор, сохраняющий переданные параметры и результаты работы функции в json-файл"""

    def decorator_func(func: Callable):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except:
            data = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data.append({"params": args, "result": result})
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            return result

        return wrapper

    return decorator_func


@quadratic_equation_from_csv('hw_task1.csv')
@save_to_json('hw_task1.json')
def quadratic_equation(a: int, b: int, c: int):
    """Функция для нахождения корней квадратного уравнения"""
    D = b ** 2 - 4 * a * c
    if D < 0:
        return "No solutions"
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
