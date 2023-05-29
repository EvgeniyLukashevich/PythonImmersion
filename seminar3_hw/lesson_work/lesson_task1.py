# Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные элементы исходного списка.
# * Подготовьте два решения, короткое и длинное,
# которые не используют другие коллекции помимо списков
import time
from random import randint as ri

origin_list = [22, 22, 3, 444, 444, 444, "Hi", "Hi", "Bro", 3.14, 3.14, True, True]
origin_list2 = [ri(1, 20) for _ in range(10000)]


# решение с использованием других коллекций (множеств)
def first_solution(inner_list: list) -> list:
    new_set = set()

    for element in inner_list:
        new_set.add(element)

    return list(new_set)


# Короткое решение без использования других коллекций, кроме списков
def second_solution(inner_list: list) -> list:
    new_list = []

    for element in inner_list:
        if element not in new_list:
            new_list.append(element)

    return new_list


# Длинное решение, без использования других коллекций, кроме списков
def third_solution(inner_list: list) -> list:
    new_list = []

    for i in range(len(inner_list)):
        is_unique = True
        for j in range(i + 1, len(inner_list)):
            if inner_list[i] == inner_list[j]:
                is_unique = False
                break
        if is_unique:
            new_list.append(inner_list[i])

    return new_list


print("Исходный список:", origin_list2, "\n")

# Захотелось посмотреть разницу во времени выполнения

start_time = time.time()
print("Первое решение:", first_solution(origin_list2))
print("Время выполнения:", (time.time() - start_time) * 1000, "миллисекунд", "\n")

start_time = time.time()
print("Второе решение:", second_solution(origin_list2))
print("Время выполнения:", (time.time() - start_time) * 1000, "миллисекунд", "\n")

start_time = time.time()
print("Третье решение:", third_solution(origin_list2))
print("Время выполнения:", (time.time() - start_time) * 1000, "миллисекунд", "\n")
