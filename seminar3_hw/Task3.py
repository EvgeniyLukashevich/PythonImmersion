# SEMINAR 3. HOMEWORK. TASK 3
# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

from itertools import combinations as combos
from pprint import pprint as pp


def bag_equips(things: dict, max_weight: float):
    result_list = []

    for i in range(len(things)):
        # установим минимальное количество вещей = 3
        for combo in combos(things.items(), i + 3):
            # среди возможных комбинаций отсечём те, что не проходят по весу
            if sum(dict(combo).values()) <= max_weight:
                result_list.append(dict(combo))

    return result_list


things_dict = {
    "фонарь": 0.5,
    "спальник": 1,
    "еда": 1.5,
    "котелок": 0.3,
    "тарелка": 0.2,
    "кружка": 0.1,
    "палатка": 2}

combo_list = bag_equips(things_dict, 3)
pp(combo_list)
